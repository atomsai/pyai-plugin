# Contributing

Keep this package focused on connecting to the public PyAI MCP endpoint and guiding real workflows. Edit skills against the connected tool schemas and https://api.pyai.com/openapi.json. Do not copy service implementation or customer data into this repository.

1. Change the relevant skill or plugin metadata.
2. Run `python3 scripts/validate.py`; use `--live` to verify public discovery and referenced tool IDs.
3. For changes to authentication or tool invocation, verify in a supported client with a user-authorized project. Do not use paid generation as an automatic smoke test.
4. Increment `.cursor-plugin/plugin.json` when publishing a plugin update. Request marketplace re-indexing as required by the host.

CI validates files on every pull request. A hosted service update does not automatically publish new plugin files or approve a marketplace listing.
