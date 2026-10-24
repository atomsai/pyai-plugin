# Connect PyAI to Cline

PyAI is a hosted MCP server for user-approved phone calls, speech, transcription,
voice agents and call analysis. This repository distributes integration metadata
and workflow skills; the service implementation is hosted by PyAI.

## Hosted connection

In Cline's MCP server settings, add a remote Streamable HTTP server named `pyai`
with URL `https://api.pyai.com/mcp`. For Cline versions using JSON settings:

```json
{
  "mcpServers": {
    "pyai": {
      "type": "streamableHttp",
      "url": "https://api.pyai.com/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Merge this entry with existing servers; do not overwrite unrelated settings.
With Cline CLI, the equivalent is:

```sh
cline mcp add pyai https://api.pyai.com/mcp --transport http --yes
```

Complete Cline's browser OAuth flow, select the intended PyAI project and review
its requested permissions. No API key or client secret belongs in this config.
Configuration installation alone does not establish an authenticated connection.

## Verify without a call or purchase

Ask Cline: “Use PyAI get_started and discover_tools with query calling. Report
whether both succeed. Do not place calls, purchase numbers, generate audio, or
read project data.” Leave automatic approval disabled. Use the connected tool
schemas for actual operations; never guess request fields.

Calls require an eligible PyAI project, `telephony:manage`, an owned caller
number, an agent and credits. Calling requires explicit user authorization;
installation does not authorize it. See the [calling workflow](skills/pyai-calling/SKILL.md).

If authentication or scopes fail, repair the connection rather than repeatedly
retrying. Never put credentials, private phone numbers or transcripts in issue
reports. Disconnect and revoke test access when finished.

Setup and support: https://pyai.com/mcp
