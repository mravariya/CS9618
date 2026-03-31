# Source ZIP inventory (Teach Cambridge export)

The archive **`CS9618S.zip`** (Teach Cambridge, March 2026) contained **37 files**. This repository **deduplicates** by:

- Keeping **one canonical syllabus series** (2027–2029) and matching **Pseudocode Guide** under `resources/references/originals/`.
- Keeping **Scheme of Work** and **Learner Guide** PDFs there as well.
- **Not** committing duplicate syllabus/pseudocode years or **exam supporting file** ZIPs by default (large, repetitive). Extract them locally if you need inserts for specific sessions.

## Files in the original ZIP

| Category | Files |
| --- | --- |
| Syllabus PDFs | 2026 syllabus; 2027–2029 syllabus |
| Pseudocode guides | 2023–2025; 2026; 2027–2029 |
| Scheme of Work | PDF + DOCX (2021 onwards) |
| Learner Guide | PDF (2021 onwards) |
| Exam supporting ZIPs | June / November 2021–2025, variants 41–43 |

## Recommended local extract

If you still have the ZIP, you can extract everything to `_source/` for personal use. The `.gitignore` in this repo ignores `_source/` so accidental commits of **all** archives are avoided.

## Copyright

Materials from Cambridge / Teach Cambridge are **not** open-licensed. This inventory is for **organisation only**. Use your centre’s licences and the School Support Hub for redistribution rights.
