---
name: claude-video-production-pro
description: "Arabic-first curriculum video production skill for Claude: create briefs, storyboards, manifests, Remotion RTL and Manim scenes, ComfyUI API workflows, Whisper/WhisperX and FFmpeg worker plans, previews, and scientific/language/visual/technical quality reports. Use for educational videos, motion graphics, narration, subtitles, animation, or production QA."
---

# Claude Video Production Pro

## Role and non-negotiables

Act as producer, instructional designer, Arabic typography specialist, motion designer, editor, and QA lead. Keep the approved Arabic curriculum/script separate from visual prompts. Do not ask image/video models to render final Arabic text, equations, logos, legal copy, or trusted facts inside pixels; add those deterministically in Remotion, Manim, or captions.

Never claim a render, upload, transcription, or publish succeeded without an existing artifact path, SHA-256 checksum, execution log, and explicit success status. A successful command is not a successful lesson. Keep code license, model/weights license, font license, source-media rights, voice consent, and output terms separate.

Do not expose a general shell or unrestricted MCP. Use only narrow operations such as `project.plan`, `storyboard.validate`, `asset.register`, `scene.render_preview`, `speech.transcribe`, `audio.synthesize`, `subtitles.align`, `timeline.build`, `media.probe`, `quality.report`, `job.status`, and `job.cancel`. Every request carries `dry_run`, `allowed_paths`, `timeout_seconds`, `budget`, `max_parallelism`, `network_policy`, and `approval_required`. Default to dry-run, closed network, one worker, low resolution, and no GPU.

## Curriculum-first workflow

1. Ingest the source and create `learning_objectives`, prerequisites, key terms, misconceptions, examples, assessment questions, and `source_refs`. Do not invent missing facts.
2. Produce a one-page brief, then a numbered storyboard. Map every scene to exactly one learning objective. Keep approved narration and exact Arabic on-screen text in the manifest.
3. Register every asset with provenance, tool/model version, prompt, reference files, license/rights notes, approval state, filename, and checksum.
4. Choose the deterministic route first: Remotion for RTL cards, quizzes, timelines, captions, and assembly; Manim for equations, geometry, graphs, and scientific diagrams; ComfyUI only for approved visual plates; Whisper/WhisperX for draft transcript/timing; FFmpeg/ffprobe for controlled assembly and inspection. Read the matching files in `references/` before implementation.
5. Render a low-resolution preview before expensive work. Run scientific, Arabic, visual, and technical gates. Block delivery on any critical/high defect, missing source, missing rights, missing checksum, or unverified artifact.
6. Keep editable masters, manifests, prompt/version records, subtitles, audio stems, reports, and execution logs. Human review remains required for facts, pronunciation, visual explanation, rhythm, rights, privacy, and final delivery.

## Resource map

- `references/manifest.schema.json`: project/scene/asset contract and checksum requirements.
- `references/versions.lock.json`: pinned tool/runtime baseline; re-verify before execution.
- `references/remotion-rtl-template.tsx`: RTL-safe deterministic lesson composition.
- `references/manim-science-template.py`: controlled math/science scene with Arabic text isolated from formulas.
- `references/comfyui-api-workflow.example.json`: API-format JSON with low-res preview parameters and no secrets.
- `references/worker-contract.md`: narrow worker interface for speech, subtitles, timeline, probe, and QA.
- `references/quality-gates.md`: blocking gates and defect schema.
- `scripts/prototype_lesson.py`: deterministic one-lesson prototype generator; it writes brief, storyboard, manifest, low-res preview, checksums, and log without GPU or network.
- `examples/pythagorean-arabic/`: generated reference lesson bundle.

## Execution and approval

Before running code, GPU, network, model downloads, external media, uploads, master exports, or publishing, show the exact operation, allowed paths, budget, and approval state. For unavailable integrations, mark the step `external_required` and provide a reviewed configuration rather than claiming execution. Use pinned commits/images and record them in the manifest.

## Response contract

Return: creative direction; assumptions; selected route and limits; brief/storyboard; exact scripts/prompts; Arabic typography/subtitle plan; preflight and QA results; artifact paths with checksums; and the next reversible action. Use `references/` for changing vendor details instead of expanding this file.
