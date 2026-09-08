# Maintaining the PyAI plugin

This public repository contains a Cursor plugin: `.cursor-plugin/plugin.json`, `mcp.json`, skills and the PyAI logo. Keep credentials, private service implementation and customer content out of it.

Validate with `python3 scripts/validate.py`. The optional `--live` check only reads public metadata and an unauthenticated MCP challenge. Use the live connected schemas for tool arguments; do not infer them from tool titles. Preserve tool identifiers when editing display copy. Never claim marketplace approval or full client compatibility from static checks alone.
