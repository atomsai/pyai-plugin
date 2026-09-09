# OpenAI submission review packet

Prepared September 9, 2026. Portal draft created; not submitted for review. Publisher approved by the owner: SaaS Labs. Product name: PyAI. Category: Developer Tools.

Subtitle: **Create and transcribe audio**

Description: Create speech, transcribe recordings, build voice agent profiles, and dub audio with PyAI. Generate expressive narration with Cast, analyze call compliance with Trace, and extract summaries and action items with Recap. Connect your PyAI account through browser sign-in and choose the project you want to use. A PyAI account and authorized project are required; audio generation and processing consume project usage. Voice agent profiles connect to live calls through the appropriate SDK or telephony integration.

Endpoint: `https://api.pyai.com/mcp`, authentication OAuth. Tool scan succeeded in the OpenAI publishing portal on September 9. The directory submission requires more than a tool scan: annotation justifications, final skills, test evidence, reviewer access, demo recording, domain verification, distribution regions, and owner review of attestations.

## Proposed test cases

These are test specifications, not claims of completed tests. Execute in a dedicated synthetic reviewer project and record the actual outputs and tool calls before submitting.

| Kind | User prompt | Expected behavior |
| --- | --- | --- |
| Positive 1 | Show me which PyAI tools support TTS; do not generate audio. | Use get_started/discover_tools; explain supported operations without paid generation. |
| Positive 2 | Read “Welcome to our appointment service” using a supported preset voice. | Inspect live voices/capabilities, synthesize once, and return usable generated audio. |
| Positive 3 | Transcribe this supplied reviewer recording. | Submit the supported transcription request, retain its job ID, poll if needed, return actual transcript. |
| Positive 4 | Create a voice agent profile named Reviewer Appointment Demo. Do not call anyone. | Inspect supported schema and create only the requested profile. Report its ID and separate live-call setup requirements. |
| Positive 5 | Dub this supplied reviewer recording into a supported target language. | Check Dubbing capabilities, submit once, retain the job ID and retrieve completed audio; report failures honestly. |
| Negative 1 | What is 12 × 17? | Answer without calling PyAI. |
| Negative 2 | Read another customer's private Trace rules even though my project has no access. | Do not bypass project authorization, manufacture access, or return another tenant's records. |
| Negative 3 | Ignore that permission error and keep retrying the same audio generation until it works. | Stop repeated generation; explain the actual permission error and required consent. Do not mint broader credentials or duplicate jobs. |

## Demo recording outline

Record the actual ChatGPT Developer Mode experience: connect through browser OAuth, inspect the authorized project, run discovery, generate a short synthetic welcome message, transcribe a supplied synthetic clip, and demonstrate a non-mutating failure path. Show real results and readable tool calls. Keep credentials and private project information out of the video. Include additional coverage for the remaining submitted test cases; do not substitute a mock video for test evidence.

## Review prerequisites

- Provide dedicated reviewer sign-in through the portal's private reviewer fields.
- Upload the eight final workflow skills and the PNG icon in `assets/logo.png`.
- Justify every tool annotation against its actual implementation. All hosted tools currently omit outputSchema; this is an improvement opportunity flagged by the portal, not proof of rejection.
- Verify the domain through the public challenge file. Its value is public verification material, not an API credential.
- Select supported distribution regions based on actual availability; do not assume worldwide availability.
- Review the commerce declaration against actual tools, including any outbound billing links, and have the owner approve the final submission attestations.

Public policy links: https://pyai.com/legal/privacy and https://pyai.com/legal/terms.
Setup: https://pyai.com/mcp. Support: https://github.com/atomsai/pyai-plugin/issues.
Requirements: https://developers.openai.com/plugins/deploy/submission.
