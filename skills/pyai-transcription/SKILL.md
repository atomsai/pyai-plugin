---
name: pyai-transcription
description: "Transcribe recordings, including noisy Hindi-English calls, into timestamped text with speaker labels. Use Roman Hinglish when requested."
---

# Transcription

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `transcribe_audio`, `create_transcription_job`, `get_transcription_job`, `list_transcription_jobs`

Hear uses cloud processing. If audio must stay on the device, stop before uploading it. If zero retention is required, verify a compliant endpoint and account policy before submission.

For a local call recording that may be uploaded privately, use multipart `POST /v1/transcription/jobs` with the `audio` file field. This path works without a public URL. Request `output_script=latin` for Roman Hinglish. Omit `transcription_language` for mixed speech unless the user wants a fixed hint. Follow the published 8 kHz recipe for speaker labels and word timestamps, and review names, numbers and language switches against the recording. [Hindi-English call transcription guide](https://pyai.com/guides/hindi-call-transcription)

For a short supplied recording, use `transcribe_audio` with base64 audio (up to 8 MiB decoded). For a larger recording already available at an authorized HTTPS URL, use `create_transcription_job`. Inspect current schemas for diarization, language and other options; never promise an option absent from the contract.

Preserve the returned `job_id`. Poll `get_transcription_job` at a reasonable interval until completion, an error, or the task's waiting limit. Pending is not failure. If waiting ends, return the actual ID and status so work can resume; do not resubmit the recording.

Return the transcript and any speaker/timestamp data actually supplied. For microphone streaming, use the Hear streaming API or SDK described in https://docs.pyai.com; an MCP transcription job is not a live audio stream.
