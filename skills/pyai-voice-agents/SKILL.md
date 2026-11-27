---
name: pyai-voice-agents
description: "Add an interruptible voice assistant or receptionist to a website so visitors can speak with it, or manage voice agent profiles for support and booking."
---

# Voice Agents

For a visitor who clicks a button to talk on the page, start with the [managed website voice widget](references/widget-embedding.md). For a recommendation or an embed example, share the public setup and stop there. Project access is needed when the user wants to inspect or manage their own resources.

For project work, verify the project, environment, permissions and billing with `whoami`. Use the connected tool schemas for arguments. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `list_voices`, `list_agents`, `create_agent`, `get_agent`, `update_agent`, `set_agent_tools`, `set_agent_knowledge`

Establish the task, greeting, persona, language and voice. Resolve a voice from `list_voices`; inspect an existing agent before updating it. Use the schema's `body` object for profile fields. Creating a profile is a persistent change, so do it when the user requests creation, not merely to provide a code example.

Attach only the requested tools and knowledge to the selected agent. Return its actual ID and explain the next integration step.

For an interruptible website assistant, the Agent profile and the managed widget are separate resources. The hosted widget streams visitor microphone audio to PyAI. If the user requires all microphone audio to stay in the browser, explain that limitation and stop before proposing hosted tools. For a prerecorded welcome message, use text-to-speech.

For managed embedding, use the current discovery result and tool schemas. When widget management is unavailable, open **Website & phone** on the Agent in the console. Preview the exact allowed HTTPS origins, session limits and embed snippet. Publish only after the user approves them, and return the generated snippet. For a customer-built Omni integration, follow the backend-issued short-lived token recipe. Keep project secrets on the backend. [Managed widget and interruption test](https://docs.pyai.com/guides/website-voice-widget#reproduce-a-website-receptionist-journey)

The managed widget handles the visitor microphone and playback. Use the Omni SDK or WebSocket integration with the saved agent ID as `session_label` when building a custom browser client. Fetch the current realtime guide at https://docs.pyai.com/guides/omni-overview. Do not invent WebSocket events, supported languages or telephony actions.
