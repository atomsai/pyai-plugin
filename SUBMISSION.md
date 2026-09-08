# Marketplace submission

Repository URL: https://github.com/atomsai/pyai-plugin

| Field | Value |
| --- | --- |
| Organization | AtomsAI |
| Organization handle | atomsai |
| Plugin | PyAI — Voice AI |
| Website | https://pyai.com/mcp |
| Logo | https://raw.githubusercontent.com/atomsai/pyai-plugin/main/assets/logo.svg |

Use a monitored contact email controlled by the submitting owner. Select the account authorized to represent AtomsAI in the marketplace form.

## Description

PyAI brings voice AI tools to your AI assistant. Build and manage voice agents, generate natural text-to-speech (TTS), transcribe audio with speech-to-text (STT), translate and dub recordings, and create expressive voiceovers. Analyze calls for compliance with Trace and generate conversation summaries and action items with Recap. Connect your PyAI project through browser sign-in, then work through natural-language requests—no API keys to paste into chat.

## Review notes

- Format: single Cursor Plugin with eight Agent Skills and one remote MCP connection.
- Authentication: client-managed browser OAuth at https://api.pyai.com/mcp.
- A PyAI account and authorized project are required. Generation consumes usage.
- The hosted MCP service was checked through actual browser OAuth and non-billable tool calls in ChatGPT and Claude on September 8, 2026. That verifies the endpoint, not marketplace installation of this new package in Cursor/Grok Bot.
- Validate this package with `python3 scripts/validate.py --live`. Reviewers can perform a non-billable client check using `get_started` and `discover_tools` with query `TTS`.
- Public marketplace approval is not claimed. Submit the repository for review at https://cursor.com/marketplace/publish.
