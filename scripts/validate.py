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


def mcp_result(endpoint, method, params):
    payload = {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}
    request = Request(endpoint, data=json.dumps(payload).encode(), headers={
        'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream',
    })
    with urlopen(request, timeout=20) as response:
        envelope = json.load(response)
    require('result' in envelope and 'error' not in envelope, f'{method} failed')
    return envelope['result']


def validate(live=False):
    manifest = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
    marketplace = json.loads((ROOT / '.cursor-plugin/marketplace.json').read_text())
    require(marketplace.get('owner', {}).get('name') == manifest['author']['name'], 'Marketplace publisher mismatch')
    require(len(marketplace.get('plugins', [])) == 1, 'Expected one marketplace plugin')
    entry = marketplace['plugins'][0]
    require(entry['name'] == manifest['name'] and local_file(entry['source']) == ROOT, 'Marketplace must resolve this plugin at the repository root')
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
    require(config == {'mcpServers': {'pyai': {'type': 'http', 'url': 'https://api.pyai.com/mcp'}}}, 'Expected only the hosted OAuth connection, without stored credentials or startup commands')
    factory = json.loads((ROOT / '.factory-plugin/plugin.json').read_text())
    for key in ('name', 'version', 'author', 'homepage', 'repository', 'license'):
        require(factory.get(key) == manifest[key], f'Factory metadata mismatch: {key}')
    factory_marketplace = json.loads((ROOT / '.factory-plugin/marketplace.json').read_text())
    require(factory_marketplace.get('owner') == factory['author'], 'Factory publisher mismatch')
    factory_entries = factory_marketplace.get('plugins', [])
    require(len(factory_entries) == 1 and factory_entries[0]['name'] == factory['name'], 'Expected one Factory plugin')
    require(local_file(factory_entries[0]['source']) == ROOT, 'Factory marketplace must resolve the root plugin')
    claude = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    claude_marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    require(claude_marketplace['name'] == 'atomsai' and claude_marketplace['owner'] == manifest['author'],
            'Unexpected Claude marketplace or publisher')
    entries = claude_marketplace['plugins']
    require(len(entries) == 1 and entries[0]['name'] == claude['name'] and local_file(entries[0]['source']) == ROOT,
            'Claude marketplace must resolve the root plugin')
    for key in ('name', 'version', 'author', 'description', 'mcpServers'):
        require(claude[key] == manifest[key], f'Claude metadata mismatch: {key}')
    skills_root = local_file(manifest['skills'])
    require(skills_root == ROOT / 'skills', 'Claude Code loads skills from the shared skills folder')
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
    openclaw_skills = sorted((ROOT / 'openclaw').glob('*/SKILL.md'))
    for skill in openclaw_skills:
        match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]+")\nmetadata: (\{[^\n]+\})\n---\n', skill.read_text())
        require(match is not None, f'{skill}: invalid OpenClaw frontmatter')
        name, description, metadata = match.group(1), json.loads(match.group(2)), json.loads(match.group(3))
        require(name == skill.parent.name and len(name) <= 64, f'{skill}: invalid skill name')
        require(isinstance(description, str) and 0 < len(description) <= 1024, f'{skill}: invalid description')
        package = metadata.get('openclaw', {})
        require(package.get('homepage') == manifest['homepage'], f'{skill}: unexpected homepage')
        require(package.get('requires') == {'bins': ['pyai']}, f'{skill}: expected the official CLI dependency')
        installers = package.get('install', [])
        require(len(installers) == 1 and installers[0].get('kind') == 'brew'
                and installers[0].get('formula') == 'atomsai/tap/pyai'
                and installers[0].get('bins') == ['pyai'], f'{skill}: unexpected CLI installer')
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
        endpoint = config['mcpServers']['pyai']['url']
        server = mcp_result(endpoint, 'initialize', {
            'protocolVersion': '2025-11-25', 'capabilities': {},
            'clientInfo': {'name': 'pyai-plugin-validation', 'version': manifest['version']},
        })
        require('tools' in server['capabilities'], 'Hosted server has no tool capability')
        tools = mcp_result(endpoint, 'tools/list', {})
        public_tools = {tool['name'] for tool in tools['tools']}
        require(referenced_tools <= public_tools, f'Tools missing from hosted server: {sorted(referenced_tools - public_tools)}')
        try:
            mcp_result(endpoint, 'tools/call', {'name': 'whoami', 'arguments': {}})
        except HTTPError as error:
            with error:
                require(error.code == 401 and 'oauth-protected-resource' in error.headers.get('WWW-Authenticate', ''),
                        'Missing OAuth challenge on project identity')
        else:
            raise ValueError('Anonymous project identity must require sign-in')
        print(f"Hosted {server['serverInfo']['version']}: {len(public_tools)} public tools. Project identity required OAuth.")
    print(f'Package checks passed: {len(skills)} MCP skills, {len(openclaw_skills)} OpenClaw skills, hosted MCP config, metadata and logo. This does not prove marketplace installation.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true', help='Read public PyAI metadata and unauthenticated MCP challenge')
    args = parser.parse_args()
    try:
        validate(args.live)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
