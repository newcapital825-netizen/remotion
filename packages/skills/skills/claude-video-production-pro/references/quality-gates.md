# Quality gates

A lesson is `blocked` when any Critical or High defect remains, when an artifact/checksum/log is missing, or when rights/consent/source provenance is unknown.

## Scientific

Check every claim against `source_refs`; verify units, equations, examples, assumptions, age appropriateness, and misconceptions. Map each scene to one objective. Mark unsupported claims `factual_question` rather than guessing.

## Arabic and captions

Check spelling, terminology, numbers, punctuation, diacritics where required, Arabic/Latin mixing, joining/shaping, RTL order, line breaks, pronunciation, captions, and audio/text agreement. Review at delivery size and mobile width.

## Visual and instructional

Each visual must explain the objective, not decorate it. Check hierarchy, contrast, safe areas, timing, legibility, continuity, motion comfort, equation layout, and that generated plates contain no final Arabic copy or factual labels.

## Technical and rights

Open the actual artifact; probe streams, duration, fps, resolution, audio sample rate, subtitle timing, and checksum. Confirm tool/model/font/source-media licenses, voice consent, AI disclosure, privacy policy, and no unapproved upload.

## Defect record

```json
{"severity":"Critical|High|Medium|Low","gate":"scientific|arabic|visual|technical|rights","scene_id":"S01","timecode":"00:00:00","description":"","owner":"","disposition":"open|fixed|accepted","evidence":"path or checksum"}
```
