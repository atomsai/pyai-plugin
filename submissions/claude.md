# Claude Directory submission packet

Prepared September 9, 2026. This is a review packet, not a submitted or approved listing. The current account cannot access the Team/Enterprise directory submission portal.

## Listing fields

| Field | Copy |
| --- | --- |
| Name | PyAI |
| Tagline | Create speech, transcribe audio, and build voice agents |
| Suggested categories | Developer tools; Productivity; Audio (choose available portal categories) |
| Website and setup | https://pyai.com/mcp |
| Documentation | https://docs.pyai.com |
| Support | https://github.com/atomsai/pyai-plugin/issues |
| Privacy | https://pyai.com/legal/privacy |
| Terms | https://pyai.com/legal/terms |
| Icon | https://raw.githubusercontent.com/atomsai/pyai-plugin/main/assets/logo.png |
| Suggested permanent slug | pyai |

## Description

Create speech, transcribe recordings, build voice agent profiles, and dub audio with PyAI. Generate expressive narration with Cast, analyze call compliance with Trace, and extract summaries and action items with Recap. Connect your PyAI account through browser sign-in and choose the project you want to use. Start by asking which tools support your task, then provide the text, audio, or authorized record you want to work with.

A PyAI account and authorized project are required. Audio generation and processing consume project usage. Supported voices, languages, and rendering options are discovered from the live service. Voice agent profiles connect to live calls through the appropriate SDK or telephony integration.

## Connection and permissions

- Streamable HTTP endpoint: `https://api.pyai.com/mcp`.
- OAuth authorization code flow, dynamic client registration, S256 PKCE, refresh-token rotation and project consent.
- Discovery: `https://api.pyai.com/.well-known/oauth-authorization-server` and `https://api.pyai.com/.well-known/oauth-protected-resource/mcp`.
- No static API key or client secret should be pasted into chat or this public repository.
- Public tool catalog: `https://pyai.com/mcp-tools.json`. There are 43 tools in the 0.3.2 catalog; scan again before submitting.
- Project operations access only the project and scopes approved through OAuth. Some tools generate billable media or change agent/configuration records. Configuration-read tools can require configure scopes that also allow writes; reviewers must inspect these permissions explicitly.
- Inputs may include scripts, audio URLs, recordings, transcripts, and project record identifiers. Outputs include generated media, transcripts, job status, agent profiles, compliance findings, and summaries. Use the published privacy policy for data handling; do not invent retention or residency guarantees.

## Demonstration prompts

1. Show me which PyAI tools support text-to-speech. Do not generate audio yet.
2. Read this welcome message aloud using a supported preset voice.
3. Transcribe this supplied recording and return its text.
4. Create an appointment-booking voice agent profile; do not start a live call.
5. Dub this supplied recording into a supported target language.
6. Summarize this authorized call and extract next steps with Recap.

## Review evidence and remaining requirements

Browser OAuth plus non-billable discovery succeeded in Claude on September 8, 2026. This is an endpoint smoke test, not an attestation that every tool has been exercised in Claude or that directory review has passed.

Before submission: use an eligible organization owner, supply the authorized company/contact details and a dedicated reviewer account, execute every tool's required review test with synthetic data, record outcomes, complete the portal's data-handling questions, and have the owner review its policy attestations. Keep reviewer credentials out of this file and out of public GitHub issues.

Portal: https://claude.ai/admin-settings/directory/submissions/new
Requirements: https://claude.com/docs/connectors/building/submission
