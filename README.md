<p align="center"><img src="assets/logo.svg" width="88" height="88" alt="PyAI logo"></p>

# PyAI — Voice AI

Voice agents, text-to-speech, transcription, call analysis, dubbing and expressive narration for AI assistants.

Connect your PyAI project with browser OAuth. Ask for the result you need in plain language; the plugin supplies the MCP connection and focused workflow skills.

[Setup guide](https://pyai.com/mcp) · [API docs](https://docs.pyai.com) · [PyAI](https://pyai.com)

## What you can do

| Capability | Example request | Skill |
| --- | --- | --- |
| Discover tools | “Show me what PyAI can do for this project.” | `pyai-get-started` |
| Voice agents | “Create an appointment-booking agent profile.” | `pyai-voice-agents` |
| Text-to-speech (TTS) | “Read this welcome message in a warm voice.” | `pyai-text-to-speech` |
| Speech-to-text (STT) | “Transcribe this interview.” | `pyai-transcription` |
| Call compliance | “Find missing recording disclosures and show the evidence.” | `pyai-call-compliance` |
| Call summaries | “Summarize this call and extract next steps.” | `pyai-call-summaries` |
| Dubbing | “Dub this recording into a supported target language.” | `pyai-dubbing` |
| Narration | “Turn this script into expressive narration with pauses.” | `pyai-narration` |

Language, voice and rendering availability come from live capabilities. MCP creates and manages voice agent profiles; live microphone and phone sessions use the appropriate SDK, realtime or telephony integration.

## Connect

This repository is a Cursor plugin package. Public marketplace submission/review is separate from publishing this repository; no marketplace approval is claimed.

For a direct MCP connection today, add this remote server in your client's MCP settings:

```json
{
  "mcpServers": {
    "pyai": {
      "url": "https://api.pyai.com/mcp"
    }
  }
}
```

Choose Connect/Sign in and complete browser OAuth. Select the intended PyAI project and review the requested scopes. No API key, client secret, local Node runtime or startup script is required for this hosted connection. A PyAI account and authorized project are required; generation consumes project usage.

After a marketplace installation, the same connection is supplied by `mcp.json`. In Grok Bot, connected apps appear under Settings → Plugins and can be attached with `@`; availability depends on the host's marketplace and account policy. A direct MCP connection loads server tools; installing this plugin also supplies the workflow skills.

## More installation options

Find the hosted MCP server on [Smithery](https://smithery.ai/servers/gaurav-ywfe/pyai). Its listing points to the same PyAI endpoint and browser sign-in flow.

For engineers and terminal-based agents, install the CLI through the [official Homebrew tap](https://github.com/atomsai/homebrew-tap):

```sh
brew install atomsai/tap/pyai
pyai login
pyai speak "Hello from PyAI" -o hello.wav
```

The speech command consumes project usage. The tap checks for new stable SDK/CLI releases every six hours; run `brew update && brew upgrade pyai` to update an installed copy. See the [CLI guide](https://pyai.com/cli) for npm installation, JSON output and automation.

## Check the connection

Ask: “Use PyAI get_started and discover_tools with query TTS. Report whether both succeed. Do not generate audio or read project data.”

For actual project operations, `whoami` identifies the authorized workspace and scopes. Tool IDs are stable even when display labels change; for example, the Dubbing status tool is `get_dub_job`.

## Local plugin preview in Cursor

Clone this repository, then open Customize → Plugins → Add → From Local Repository and select the checkout. The included marketplace manifest points to the plugin at the repository root. Follow [Cursor's current plugin instructions](https://cursor.com/docs/reference/plugins). Grok Bot marketplace installation is a separate path; a local Cursor preview does not establish Grok Bot availability.

## Data and permissions

The package contains connection metadata, skills and a logo. It contains no backend implementation or credentials. Requests are processed by the hosted PyAI service within the project access you approve. Client tool permissions and PyAI project scopes both apply. Disconnect/revoke access through the host and PyAI account controls when no longer needed.

Trace/Recap configuration reads may require configure scopes that also allow writes. The skills distinguish reading results from changing configuration. Audio generation and other paid operations are performed for the user's task, not as automatic onboarding tests. Pending jobs retain their IDs to avoid duplicate submissions.

## Troubleshooting

- **Not connected:** complete OAuth in the host. Do not paste credentials into chat.
- **Missing scope:** review project consent for the requested operation. Retrying does not add permission.
- **Usage/credit error:** resolve project billing or limits before retrying.
- **Old labels or missing tools:** refresh the connector's tools list.
- **Pending media job:** retain its ID and poll the status tool rather than submitting again.

## Maintain and validate

Run `python3 scripts/validate.py` for package checks, and `python3 scripts/validate.py --live` to also check public OAuth discovery, the unauthenticated MCP challenge and the live tool IDs referenced by skills. Neither command creates credentials or consumes generation usage.

The plugin version tracks changes to these files. The hosted MCP service updates independently; clients may need to refresh their tool catalog. This package does not vendor a fixed API schema. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance and [SUBMISSION.md](SUBMISSION.md) for marketplace form details.

## Support

Use [GitHub issues](https://github.com/atomsai/pyai-plugin/issues) for plugin packaging and workflow guidance. Do not include tokens, private transcripts or customer recordings in public issues. Account help and product documentation are available through [PyAI](https://pyai.com).

## License

MIT for the integration files. The PyAI name and logo identify the service; the software license does not grant trademark rights or rights to user content.
