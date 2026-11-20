# Narrow worker contract

Expose typed operations, never a general shell. Each request must include:

```json
{"dry_run":true,"allowed_paths":["project/audio","project/subtitles","project/dist"],"timeout_seconds":600,"budget":{"gpu_seconds":0,"api_credits":0,"max_files":20},"max_parallelism":1,"network_policy":"closed","approval_required":true}
```

Allowed operations:

- `speech.transcribe`: local audio -> draft JSON transcript with language, model revision, segments, and checksum.
- `subtitles.align`: approved transcript + audio -> SRT/VTT with word/segment timing; mark Arabic terminology as `human_review_required`.
- `audio.synthesize`: only an approved local/provider adapter; record consent, provider, voice, model, and retention policy. No voice cloning without explicit consent.
- `timeline.build`: approved scene manifest + media -> deterministic FFmpeg/Remotion plan; no arbitrary filter strings.
- `media.probe`: allowlisted `ffprobe` fields -> stream/duration/codec report.
- `quality.report`: manifest + reports -> blocking defect log and approval status.

Return `{job_id, status, artifacts:[{path, sha256}], logs:[...], external_required}`. A worker must write an append-only JSONL execution record. Do not log secrets, raw student data, or full private audio.
