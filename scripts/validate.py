#!/usr/bin/env python3
"""Validate this plugin's packaging; --live adds public, non-billable checks."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_file(value):
    require(isinstance(value, str) and not Path(value).is_absolute(), 'Expected a relative package path')
    path = (ROOT / value).resolve()
    require(path.is_relative_to(ROOT) and path.exists(), f'Missing or escaping package path: {value}')
    return path


def public_json(url):
    with urlopen(Request(url, headers={'User-Agent': 'pyai-plugin-validation/0.1.0'}), timeout=20) as response:
        return json.load(response)


def validate(live=False):
    manifest = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
    require(re.fullmatch(r'[a-z0-9]+(?:[.-][a-z0-9]+)*', manifest['name']), 'Invalid plugin name')
    require(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Invalid release version')
    require(manifest.get('description') and manifest.get('author', {}).get('name'), 'Missing publisher metadata')
    require(isinstance(manifest.get('keywords'), list) and all(isinstance(k, str) for k in manifest['keywords']), 'Invalid keywords')
    require(manifest['repository'] == 'https://github.com/atomsai/pyai-plugin', 'Unexpected repository')
    require(manifest['homepage'] == 'https://pyai.com/mcp', 'Unexpected homepage')
    logo = ElementTree.parse(local_file(manifest['logo'])).getroot()
    view = logo.attrib['viewBox'].split()
    require(len(view) == 4 and float(view[2]) == float(view[3]), 'Logo must be square')
    require(logo.find('{http://www.w3.org/2000/svg}rect') is not None, 'Logo needs a background plate')
    config = json.loads(local_file(manifest['mcpServers']).read_text())
    require(config == {'mcpServers': {'pyai': {'url': 'https://api.pyai.com/mcp'}}}, 'Expected only the hosted OAuth connection, without stored credentials or startup commands')
    skills_root = local_file(manifest['skills'])
    skills = sorted(skills_root.glob('*/SKILL.md'))
    require(skills, 'No skills found')
    names, referenced_tools = set(), set()
    for skill in skills:
        text = skill.read_text()
        match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]+")\n---\n', text)
        require(match is not None, f'{skill}: use plain name and JSON-quoted description in YAML frontmatter')
        name, description = match.group(1), json.loads(match.group(2))
        require(name == skill.parent.name and name not in names and len(name) <= 64, f'{skill}: invalid or duplicate name')
        require(isinstance(description, str) and 0 < len(description) <= 1024, f'{skill}: invalid description')
        require(len(text[match.end():].strip()) > 80 and '[TODO' not in text, f'{skill}: unfinished instructions')
        names.add(name)
        tool_line = re.search(r'^Tools: (.+)$', text, re.MULTILINE)
        require(tool_line is not None, f'{skill}: missing referenced tools')
        referenced_tools.update(re.findall(r'`([a-z0-9_]+)`', tool_line.group(1)))
    for path in ROOT.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts:
            continue
        require(not path.is_symlink(), f'Unexpected symlink: {path}')
        require(not path.name.startswith('.env') or path.name == '.env.example', f'Environment file in package: {path}')
        if path.is_file():
            require(path.resolve().is_relative_to(ROOT), f'Escaping file: {path}')
            if path.suffix in {'.json', '.md', '.yml', '.svg'}:
                text = path.read_text()
                require(not re.search(r'pyai_(?:live|test)_[A-Za-z0-9_-]{12,}|-----BEGIN .*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}', text), f'Possible credential in {path}')
    if live:
        catalog = public_json('https://pyai.com/mcp-tools.json')
        available = {tool['name'] for tool in catalog['tools']}
        require(referenced_tools <= available, f'Unknown hosted tools: {sorted(referenced_tools - available)}')
        resource = public_json('https://api.pyai.com/.well-known/oauth-protected-resource/mcp')
        require(resource['resource'] == config['mcpServers']['pyai']['url'], 'OAuth resource mismatch')
        require(resource['authorization_servers'] == ['https://api.pyai.com'], 'Unexpected authorization server')
        oauth = public_json('https://api.pyai.com/.well-known/oauth-authorization-server')
        require(oauth['registration_endpoint'] == 'https://api.pyai.com/auth/mcp/register', 'DCR endpoint mismatch')
        require('S256' in oauth['code_challenge_methods_supported'], 'PKCE S256 unavailable')
        request = Request(config['mcpServers']['pyai']['url'], data=json.dumps({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'pyai-plugin-validation','version':'0.1.0'}}}).encode(), headers={'Content-Type':'application/json','Accept':'application/json, text/event-stream'})
        try:
            with urlopen(request, timeout=20):
                raise ValueError('Expected unauthenticated MCP to return 401')
        except HTTPError as error:
            require(error.code == 401 and 'oauth-protected-resource' in error.headers.get('WWW-Authenticate', ''), 'Missing OAuth challenge')
            error.close()
        print(f'Public checks passed: {len(referenced_tools)} referenced tool IDs, OAuth discovery and MCP challenge. No authenticated or paid calls.')
    print(f'Package checks passed: {len(skills)} skills, hosted MCP config, metadata and logo. This does not prove marketplace installation.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true', help='Read public PyAI metadata and unauthenticated MCP challenge')
    args = parser.parse_args()
    try:
        validate(args.live)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
