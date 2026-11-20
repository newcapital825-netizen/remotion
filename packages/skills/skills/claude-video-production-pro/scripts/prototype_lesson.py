#!/usr/bin/env python3
"""Generate a no-network, no-GPU Arabic lesson prototype and auditable artifacts."""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, time
from pathlib import Path

LESSON = {
    "project_id": "pythagorean-arabic",
    "title": "نظرية فيثاغورس",
    "objective": "أن يربط المتعلم بين أطوال أضلاع المثلث القائم والعلاقة a² + b² = c².",
    "source_ref": "مصدر المنهج: يُستبدل بمرجع كتاب/صفحة معتمد قبل التسليم.",
    "scenes": [
        {"scene_id":"S01","title":"السؤال","duration_seconds":4,"narration":"كيف نحسب طول الضلع المجهول في مثلث قائم؟","text":"كيف نحسب الضلع المجهول؟","visual":"triangle_intro"},
        {"scene_id":"S02","title":"العلاقة","duration_seconds":5,"narration":"في المثلث القائم، مربع الوتر يساوي مجموع مربعي الضلعين القائمين.","text":"a² + b² = c²","visual":"manim_formula"},
        {"scene_id":"S03","title":"مثال","duration_seconds":6,"narration":"إذا كان الضلعان القائمان ثلاثة وأربعة، فالوتر يساوي خمسة.","text":"3² + 4² = 5²","visual":"deterministic_example"},
        {"scene_id":"S04","title":"تحقق","duration_seconds":4,"narration":"اسأل نفسك: هل المثلث قائم؟ ثم عوّض بالقيم وتحقق من الوحدة.","text":"تحقق: قائم؟ عوّض. راجع الوحدة.","visual":"remotion_summary"},
    ],
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def write(path: Path, content: str | bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))

def make_ppm(path: Path, width: int, height: int, scene_index: int):
    # Simple geometric animatic frame; Arabic text is rendered deterministically later.
    palette = [(8,17,31),(13,42,57),(24,55,70),(16,45,54)]
    bg = palette[scene_index % len(palette)]
    pixels = bytearray()
    for y in range(height):
        for x in range(width):
            accent = (79,209,197) if ((x - width//2)**2 + (y-height//2)**2) < (min(width,height)//4)**2 else (0,0,0)
            if accent != (0,0,0): pixels.extend(accent)
            else: pixels.extend(bg)
    write(path, f"P6\n{width} {height}\n255\n".encode() + pixels)

def render_preview(out: Path, fps: int = 12):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return False, "ffmpeg_not_found"
    frames = out / "_frames"
    frames.mkdir(parents=True, exist_ok=True)
    frame_number = 0
    for i, scene in enumerate(LESSON["scenes"]):
        count = scene["duration_seconds"] * fps
        for n in range(count): make_ppm(frames / f"frame_{i:03d}_{n:04d}.ppm", 512, 288, i)
        for n in range(count):
            (frames / f"frame_{i:03d}_{n:04d}.ppm").rename(frames / f"frame_{frame_number:05d}.ppm")
            frame_number += 1
    target = out / "dist" / "preview_512x288.mp4"
    target.parent.mkdir(parents=True, exist_ok=True)
    cmd = [ffmpeg, "-y", "-framerate", str(fps), "-i", str(frames / "frame_%05d.ppm"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(target)]
    result = subprocess.run(cmd, cwd=out, capture_output=True, text=True, timeout=120)
    shutil.rmtree(frames, ignore_errors=True)
    if result.returncode != 0: return False, result.stderr[-500:]
    return True, str(target.relative_to(out))

def main():
    ap = argparse.ArgumentParser(description="Generate auditable Arabic lesson prototype")
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--render-preview", action="store_true")
    args = ap.parse_args()
    out = args.output.resolve(); out.mkdir(parents=True, exist_ok=True)
    started = time.time()
    brief = f"# Creative brief: {LESSON['title']}\n\n- الهدف: {LESSON['objective']}\n- الجمهور: متعلمو الرياضيات في المرحلة المتوسطة\n- اللغة: العربية الفصحى، RTL\n- المدة: {sum(s['duration_seconds'] for s in LESSON['scenes'])} ثانية\n- المسار: Remotion RTL + Manim للمعادلة + FFmpeg للمعاينة\n- المرجع: {LESSON['source_ref']}\n- قيد: لا نص عربي داخل مخرجات النموذج التوليدي؛ النص طبقة حية قابلة للمراجعة.\n"
    storyboard = {"project_id": LESSON["project_id"], "status": "draft", "scenes": LESSON["scenes"]}
    write(out / "brief" / "creative-brief.md", brief)
    write(out / "storyboard" / "storyboard.json", json.dumps(storyboard, ensure_ascii=False, indent=2))
    write(out / "script" / "approved-narration-ar.json", json.dumps({"locale":"ar","rtl":True,"scenes": [{"scene_id":s["scene_id"],"text":s["narration"]} for s in LESSON["scenes"]]}, ensure_ascii=False, indent=2))
    write(out / "scenes" / "scene-plan.json", json.dumps({"route":"remotion+manim+ffmpeg","scenes": LESSON["scenes"]}, ensure_ascii=False, indent=2))
    preview_status = "not_requested"
    preview_detail = None
    if args.render_preview:
        ok, detail = render_preview(out)
        preview_status, preview_detail = ("success", detail) if ok else ("blocked", detail)
    else:
        preview_status = "external_required"
        preview_detail = "rerun with --render-preview after approval"
    quality = {"status":"blocked", "blocking_reasons":["source reference placeholder requires subject-matter verification", "Arabic pronunciation and subtitle timing require human review"], "gates":{"scientific":"human_review_required","arabic":"human_review_required","visual":"draft_preview_only","technical":preview_status}}
    write(out / "review" / "quality-report.json", json.dumps(quality, ensure_ascii=False, indent=2))
    artifact_paths = [out / "brief" / "creative-brief.md", out / "storyboard" / "storyboard.json", out / "script" / "approved-narration-ar.json", out / "scenes" / "scene-plan.json", out / "review" / "quality-report.json"]
    if preview_status == "success": artifact_paths.append(out / preview_detail)
    artifact_records = [{"path": str(p.relative_to(out)), "kind": p.suffix.lstrip("."), "status":"success", "sha256":sha256(p)} for p in artifact_paths if p.exists()]
    manifest = {"schema_version":"1.0.0","project_id":LESSON["project_id"],"locale":"ar","rtl":True,"learning_objectives":[LESSON["objective"]],"source_refs":[LESSON["source_ref"]],"scenes":[{**s,"narration_ar":s.pop("narration"),"on_screen_text_ar":s.pop("text"),"visual_method":s.pop("visual"),"acceptance_criteria":["objective is visible","Arabic text is deterministic","human review required"]} for s in [dict(x) for x in LESSON["scenes"]]],"profile":{"width":1920,"height":1080,"fps":30,"preview_width":512,"preview_height":288},"approvals":{"scientific":"pending","arabic":"pending","visual":"pending","technical":"pending"},"tool_versions":{"prototype_generator":"1.0.0","ffmpeg":"record_from_ffprobe"},"artifacts":artifact_records,"checksums":{r["path"]:r["sha256"] for r in artifact_records}}
    write(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    log = {"status":"success","operation":"prototype_lesson","dry_run":False,"allowed_paths":["brief","storyboard","script","scenes","review","dist","logs"],"timeout_seconds":120,"budget":{"gpu_seconds":0,"api_credits":0},"max_parallelism":1,"network_policy":"closed","approval_required":True,"preview_status":preview_status,"preview_detail":preview_detail,"elapsed_seconds":round(time.time()-started,3)}
    write(out / "logs" / "execution.json", json.dumps(log, ensure_ascii=False, indent=2))
    all_files = sorted(p for p in out.rglob("*") if p.is_file() and p.name != "checksums.sha256")
    write(out / "checksums.sha256", "".join(f"{sha256(p)}  {p.relative_to(out)}\n" for p in all_files))
    print(json.dumps({"status":"success","output":str(out),"preview":preview_status,"artifacts":len(all_files)}, ensure_ascii=False))

if __name__ == "__main__": main()
