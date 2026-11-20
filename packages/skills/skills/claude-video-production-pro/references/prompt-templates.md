# Reusable production templates

## Creative brief prompt

```text
حوّل المعلومات التالية إلى Creative Brief احترافي من صفحة واحدة.
المشروع: [الاسم]
الهدف التجاري/التعليمي: [الهدف]
الجمهور: [الجمهور]
المنصة والمقاس: [YouTube/Shorts/Reels/...]
المدة: [ثوانٍ]
اللغة واللهجة: [اللغة]
الرسالة الواحدة: [الرسالة]
CTA: [الدعوة]
المرجع البصري: [روابط/وصف]
الألوان والخطوط: [الهوية]
المواد المتاحة: [صور/فيديو/شعار/صوت]
القيود القانونية أو التقنية: [القيود]
أخرج: treatment، visual direction، risks، acceptance criteria، وقائمة أسئلة لا تتجاوز 5 أسئلة.
```

## Shot-list prompt

```text
حوّل الـCreative Brief إلى shot list مرقمة.
لكل لقطة أخرج: ID، المدة، الغرض، framing، subject، action، camera movement، lighting، background، reference assets، exact on-screen text، negative constraints، continuity links، generation/editing method، acceptance criteria.
لا تجعل أي لقطة أطول من [المدة] دون سبب. افصل بين النص الذي سيولد داخل الصورة والنص الذي يجب إضافته لاحقًا في After Effects/Premiere/Resolve.
```

## Generative-video prompt pattern

```text
[نوع اللقطة]، [الموضوع والوصف الثابت]، [الفعل الزمني المحدد]، [حركة الكاميرا]، [العدسة/المنظور]، [الإضاءة]، [البيئة]، [الإيقاع]، [الطابع البصري].
استمرارية: [الشخصية/المنتج/اللون/الاتجاه].
لا يوجد نص أو شعار أو علامة مائية أو تشوه في اليدين/الوجه أو تغير في الهوية.
المدة: [x] ثوانٍ. النسبة: [x:x].
```

## Production manifest fields

```json
{
  "asset_id": "S01_TK03",
  "project": "PROJECT_NAME",
  "shot_id": "S01",
  "source_type": "generated|licensed_stock|original|client_asset",
  "tool": "tool name",
  "model": "model/version",
  "prompt": "verbatim prompt",
  "references": ["file names or URLs"],
  "plan_or_license": "plan and license checked",
  "rights_notes": "faces, voice, logo, music, commercial use",
  "status": "draft|approved|rejected",
  "final_filename": "S01_TK03_v02.mov"
}
```

## Arabic-title checklist

Before approval, check the exact Arabic spelling, shaping and joining, RTL paragraph direction, punctuation placement, Arabic versus Latin numerals, diacritics, line breaks, font coverage, contrast, safe areas, and readability at phone size. Keep legal copy and brand names as deterministic text layers rather than model-generated pixels.

## Final-review prompt

```text
راجع الفيديو/المشروع كمدير جودة في شركة إنتاج.
أخرج defect log مرتبًا حسب Critical / High / Medium / Low.
افحص: القصة، الإيقاع، الاستمرارية، الحركة، النص العربي وRTL، الترجمة، الصوت، اللون، safe areas، العلامة التجارية، حقوق الأصول، AI disclosure، المواصفات التقنية، وأخطاء التصدير.
لكل عيب: timecode أو asset ID، الوصف، سبب المشكلة، الإجراء المقترح، والمالك.
لا تقل Ready for delivery إلا إذا لم توجد Critical أو High defects.
```

## Arabic curriculum decomposition prompt

```text
حلّل المادة التعليمية التالية دون اختراع معلومات.
أخرج JSON يحتوي على: course, unit, lesson, learning_objectives, prerequisites, key_terms_ar, misconceptions, examples, assessment_questions, source_refs, scenes.
اربط كل مشهد بهدف تعلم واحد فقط. لكل مشهد أخرج: scene_id، objective، approved_narration_ar، on_screen_text_ar، visual_type، visual_prompt_en، assets، duration_seconds، subtitle_text، acceptance_criteria، reviewer_required.
افصل النص العربي المعتمد عن prompt الصورة/الفيديو. لا تجعل نموذج الفيديو يرسم النص العربي النهائي داخل الصورة.
```

## Execution request contract

```json
{
  "dry_run": true,
  "allowed_paths": ["project/scenes", "project/derived", "project/logs"],
  "timeout_seconds": 600,
  "budget": {"gpu_seconds": 0, "api_credits": 0, "max_files": 20},
  "max_parallelism": 1,
  "network_policy": "closed",
  "approval_required": true,
  "operation": "scene.render_preview"
}
```

## Educational review prompt

```text
راجع هذا الدرس كخبير مادة ومعلم لغة عربية ومصمم تعليمي.
تحقق من: صحة المفاهيم، كفاية المثال، عدم وجود قفزة معرفية، تطابق الصوت مع النص، وضوح الرسم، اتجاه RTL، المصطلحات والأرقام والوحدات، توقيت captions، وملاءمة العمر.
أخرج: critical_errors، factual_questions، language_corrections، visual_corrections، timing_corrections، approval_status.
لا تعتبر المقطع جاهزًا إذا بقي خطأ علمي أو لغوي حرج.
```
