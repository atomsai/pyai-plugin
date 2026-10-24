<p align="center"><img src="assets/logo.svg" width="88" height="88" alt="PyAI logo"></p>

# PyAI — Voice AI

Give your AI assistant a phone. Make user-approved calls, generate speech, transcribe audio, and retrieve available call summaries. PyAI also supports voice agent profiles, dubbing, call analysis and expressive narration.

Connect your PyAI project with browser OAuth. Ask for the result you need in plain language; the plugin supplies the MCP connection and focused workflow skills.

[Setup guide](https://pyai.com/mcp) · [API docs](https://docs.pyai.com) · [PyAI](https://pyai.com)

## What you can do

| Capability | Example request | Skill |
| --- | --- | --- |
| Discover tools | “Show me what PyAI can do for this project.” | `pyai-get-started` |
| Phone calls | “Prepare a call to this number and show me the details before dialing.” | `pyai-calling` |
| Voice agents | “Create an appointment-booking agent profile.” | `pyai-voice-agents` |
| Text-to-speech (TTS) | “Read this welcome message in a warm voice.” | `pyai-text-to-speech` |
| Speech-to-text (STT) | “Transcribe this interview.” | `pyai-transcription` |
| Call compliance | “Find missing recording disclosures and show the evidence.” | `pyai-call-compliance` |
| Call summaries | “Summarize this call and extract next steps.” | `pyai-call-summaries` |
| Dubbing | “Dub this recording into a supported target language.” | `pyai-dubbing` |
| Narration | “Turn this script into expressive narration with pauses.” | `pyai-narration` |

Language, voice and rendering availability come from live capabilities. MCP can place explicitly authorized phone calls through managed telephony. Calls require an eligible project, telephony permissions, an owned caller number, an agent and sufficient credits. Creating an agent profile does not start a call. Live microphone sessions use the realtime SDK.

## Connect

This repository contains native Cursor and Factory plugin metadata with nine shared workflow skills. Public marketplace submission/review is separate from publishing this repository; no marketplace approval is claimed.

For a direct MCP connection today, add this remote server in your client's MCP settings:

```json
{
  "mcpServers": {
    "pyai": {
      "type": "http",
      "url": "https://api.pyai.com/mcp"
    }
  }
}
```

Choose Connect/Sign in and complete browser OAuth. Select the intended PyAI project and review the requested scopes. No API key, client secret, local Node runtime or startup script is required for this hosted connection. A PyAI account and authorized project are required; generation consumes project usage.

After a marketplace installation, the same connection is supplied by `mcp.json`. In Grok Bot, connected apps appear under Settings → Plugins and can be attached with `@`; availability depends on the host's marketplace and account policy. A direct MCP connection loads server tools; installing this plugin also supplies the workflow skills.

## More installation options

For Cline, follow [llms-install.md](llms-install.md) for the hosted Streamable HTTP configuration, browser sign-in and a discovery-only check. The Cline marketplace submission is separate from direct installation.

### PyAI Voice & Speech for OpenClaw

Give your assistant a voice, ears and the ability to make approved phone calls. These focused skills use the official PyAI CLI; each can be installed independently and does not automatically install an MCP connection.

| Skill | Ask your assistant | Requirements |
| --- | --- | --- |
| [Hear](openclaw/pyai-hear/SKILL.md) | “Transcribe this voice note.” | Supplied audio; `hear:transcribe`, or `transcribe:jobs` for URL jobs |
| [Speak](openclaw/pyai-speak/SKILL.md) | “Make an audio version of this briefing.” | Requested text; `speak:synthesize` |
| [Recap](openclaw/pyai-recap/SKILL.md) | “Summarize this customer conversation and show its action items.” | Existing recap ID or timed customer/agent utterances; `recap:read` and Recap enabled |
| [Calling](openclaw/pyai-calling/SKILL.md) | “Prepare a call and show me the details before dialing.” | Explicit call authorization, eligible project, `telephony:manage`, owned number, agent and credits |

Hear, Speak and Recap do not require a phone number or telephony permission. Sign in with `pyai login`; processing uses the selected project's credits and permissions. Use only the input the user selected for the task. Generated audio and summaries can be returned to the user; sending them to someone else needs separate authorization.

Each folder under `openclaw/` is a standalone skill package. Hear, Speak and Recap 1.0.0 are publicly available on ClawHub. Install the specific skill with `clawhub install @atomsai/pyai-hear`, `clawhub install @atomsai/pyai-speak`, or `clawhub install @atomsai/pyai-recap`. Repository changes and later versions are not automatically published to ClawHub. The existing calling submission is separate and unchanged; do not bypass its review hold.

For a reproducible OpenClaw test, use an isolated workspace and an explicit skill reference, for example `openclaw agent --local --agent main --message '$pyai-hear Transcribe the audio file /absolute/path/clip.wav'`. Confirm the agent actually reads the installed `SKILL.md`: a successful CLI command alone does not prove that the skill was loaded. Skill names such as `pyai-hear` are not shell commands. The commands are `pyai transcribe`, `pyai speak`, and `pyai recap get` / `pyai request`. Keep the normal host tool and permission controls in place.

The first Voice & Speech release covers Hear, Speak and Recap. Cast, Dub, Trace and realtime Omni are not included in these three skills. Live microphone conversations require an audio/SDK integration; neither a speech file nor a Recap summary establishes realtime support.

The [validation record](openclaw/validation.json) identifies the tested skill hashes, live synthetic CLI results, OpenClaw host runs, recovery fixtures and complete static/semantic scans. It distinguishes direct CLI success from actual skill loading and records failures and corrections. Physical speaker playback has not been verified.

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

## Install in Factory Droid

With [Droid installed](https://docs.factory.ai/droid-cli/quickstart), register this public repository and install the plugin:

```sh
droid plugin marketplace add atomsai/pyai-plugin
droid plugin marketplace list
droid plugin install pyai@pyai-plugin --scope user
```

Droid derives the registered marketplace name from the repository name. If you pin a tag or commit, read the name from `marketplace list` and use it after `pyai@`. Restart Droid, open `/mcp`, and complete PyAI OAuth for the intended project. Begin with the non-generating connection check above. Use `/plugins` to inspect the installed package and its skills.

For MCP tools alone, use `droid mcp add pyai https://api.pyai.com/mcp --type http` instead. Avoid configuring the endpoint twice. Factory's managed connector catalog has a separate review process; installing from this repository does not establish catalog approval. See [Factory's plugin documentation](https://docs.factory.ai/harness/plugins).

## Emergent custom MCP

In Emergent, open **Advanced controls → Select MCP Tools → New MCP Server**. Name it PyAI and paste the hosted HTTP JSON from Connect, then choose **Verify and Save**. On September 20, 2026, Emergent accepted this configuration, but enabling it required a paid plan. Authentication and tool execution in Emergent remain unverified; a saved configuration alone does not prove that OAuth works. See [Emergent's MCP instructions](https://help.emergent.sh/mcp-model-context-protocol).

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
