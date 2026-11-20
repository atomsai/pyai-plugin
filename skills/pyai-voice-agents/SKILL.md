---
name: pyai-voice-agents
description: "Add an interruptible voice assistant or receptionist to a website so visitors can speak with it, or manage voice agent profiles for support and booking."
---

# Voice Agents

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `list_voices`, `list_agents`, `create_agent`, `get_agent`, `update_agent`, `set_agent_tools`, `set_agent_knowledge`

Establish the task, greeting, persona, language and voice. Resolve a voice from `list_voices`; inspect an existing agent before updating it. Use the schema's `body` object for profile fields. Creating a profile is a persistent change, so do it when the user requests creation, not merely to provide a code example.

Attach only the requested tools and knowledge to the selected agent. Return its actual ID and explain the next integration step.

For an interruptible website assistant, the Agent profile and the managed widget are separate resources. The hosted widget streams visitor microphone audio to PyAI. If the user requires all microphone audio to stay in the browser, explain that limitation and stop before proposing hosted tools. For a prerecorded welcome message, use text-to-speech.

For managed embedding, use the current discovery result and tool schemas. When widget management is unavailable, open **Website & phone** on the Agent in the console. Preview the exact allowed HTTPS origins, session limits and embed snippet. Publish only after the user approves them, and return the generated snippet. For a customer-built Omni integration, follow the backend-issued short-lived token recipe. Keep project secrets on the backend. [Managed widget and interruption test](https://docs.pyai.com/guides/website-voice-widget#reproduce-a-website-receptionist-journey)

MCP manages profiles; it does not itself start a microphone session or place a phone call. For a live conversation, use the Omni SDK or WebSocket integration with the saved agent ID as `session_label`. Fetch the current realtime guide at https://docs.pyai.com/guides/omni-overview. Do not invent WebSocket events, supported languages or telephony actions.
