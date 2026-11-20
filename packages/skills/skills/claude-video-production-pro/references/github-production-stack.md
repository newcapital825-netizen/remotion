# GitHub production stack for Arabic curriculum video

Read this file when the request needs open-source generation, local/private execution, reproducible rendering, GitHub repository selection, or a current implementation route. Repository activity and licenses change; verify the official page and pinned commit before execution.

## Recommended core

**ComfyUI** is the orchestration layer for node-based image/video/audio workflows. Its official documentation includes Comfy MCP for Claude Desktop/Claude Code, local and cloud routes, API v2, CLI, SDKs, and JSON workflows. Pin a stable release, use official templates, isolate custom nodes, and keep API keys outside the project.

**Remotion** is the deterministic template/render layer for educational cards, objectives, diagrams, timelines, captions, quizzes, and platform variants. It works with React/TypeScript and Claude Code skills. It is not a video-generation model; it renders the code and data. Review the current Remotion license before batch or product use.

**Manim Community Edition** is the specialist layer for mathematics, science, equations, geometry, graphs, and explanatory animations. It supports Python CLI rendering, Docker, Text/MarkupText, LaTeX/MathTex, and Typst. Use Arabic text with tested fonts and test RTL shaping in actual frames. It is not a TTS or curriculum-authoring engine.

**FFmpeg** and **ffprobe** are the deterministic media layer for assembly, transcoding, audio mixing, subtitle muxing, and technical inspection. Use them after rendering and before delivery. Never treat a successful command as proof of a correct lesson; inspect the artifact and run quality gates.

**Whisper/WhisperX** provide transcription, word timing, alignment, and draft subtitles. They are not a substitute for an Arabic reviewer. Verify names, terminology, numbers, diacritics, pauses, and code-switched words. Keep audio local when privacy matters.

## Generative video models

Use **Wan2.1/VACE**, **HunyuanVideo-1.5**, **LTX-2.5**, or **CogVideoX** as optional short-shot workers. The safest curriculum pattern is: approved Arabic script and storyboard -> visual prompt and reference board -> short generation -> human review -> deterministic Arabic titles, narration, diagrams, and captions in Remotion/Manim/FFmpeg. Do not ask the model to render final Arabic text or trusted scientific facts inside pixels.

Start at low resolution and short duration. Save seed, model revision, prompt, references, hardware, and license. Treat open-source model code licenses and model-weight licenses as separate. Some repositories have regional or commercial restrictions, are experimental, or require large GPUs; check before any deployment.

## Practical Claude routes

1. **MCP route:** connect the official Comfy MCP or another vendor-published connector. Expose narrow tools, not a general shell. Return `job_id`, output paths, logs, checksums, and cost/limits.
2. **CLI route:** Claude Code writes or edits JSON, React/TypeScript, Manim Python, FFmpeg commands, SRT, and manifests. A local worker runs only allowlisted commands in a sandbox.
3. **API route:** a secure server stores credentials, submits jobs, polls status, downloads results, and writes metadata. Claude sees the job interface, not secrets.
4. **File route:** when no connector exists, Claude creates a reproducible project bundle and a dry-run command. The user reviews and runs it, then returns artifacts for QA.

## Official repositories

- ComfyUI: https://github.com/Comfy-Org/ComfyUI
- Comfy docs/MCP: https://docs.comfy.org/agent-tools/mcp.md
- Comfy CLI: https://github.com/Comfy-Org/comfy-cli
- Comfy MCP: https://github.com/Comfy-Org/comfy-mcp
- Wan2.1: https://github.com/Wan-Video/Wan2.1
- VACE: https://github.com/ali-vilab/VACE
- HunyuanVideo-1.5: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- HunyuanVideo-I2V: https://github.com/Tencent-Hunyuan/HunyuanVideo-I2V
- LTX-2: https://github.com/Lightricks/LTX-2
- LTX-2.5 docs/MCP: https://docs.ltx.io/models/ltx-2-5 and https://docs.ltx.io/_mcp/server
- CogVideo: https://github.com/zai-org/CogVideo
- Remotion: https://github.com/remotion-dev/remotion
- Remotion skills: https://github.com/remotion-dev/skills
- ManimCE: https://github.com/ManimCommunity/manim
- FFmpeg: https://github.com/FFmpeg/FFmpeg
- Whisper: https://github.com/openai/whisper
- WhisperX: https://github.com/m-bain/whisperX
- Arabic TTS research project: https://github.com/nipponjo/tts-arabic-pytorch
- Claude Code Video Toolkit: https://github.com/digitalsamba/claude-code-video-toolkit

## Security minimum

Run as a non-root user with pinned dependencies, restricted filesystem paths, no secrets in prompts, closed network by default, file size and duration limits, timeouts, GPU budgets, and audit logs. Treat Python, JavaScript, shell, custom nodes, model downloads, Docker images, `.blend` files, and media parsers as executable or potentially unsafe. Review third-party licenses, model terms, and data retention before commercial or student-data use.
