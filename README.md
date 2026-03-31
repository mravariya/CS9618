# Cambridge CIE CS9618 Open Learning Repository

Open, structured learning materials aligned with **Cambridge International AS & A Level Computer Science (9618)**. This project turns syllabus-aligned sources into **student-friendly Markdown**, clear **unit maps**, and spaces for **teacher collaboration**—supporting **UN Sustainable Development Goal 4 (Quality Education)** through reusable, openly licensed notes and activities.

> **Disclaimer:** This is an independent educational resource. It is **not** affiliated with or endorsed by Cambridge Assessment International Education. Always use the **official syllabus** and **School Support Hub** materials for authoritative assessment details. See [LICENSE](LICENSE) for the MIT license and third-party/educational-use notice.

## Purpose

- **Open-source learning platform** — Version-controlled content anyone can fork, translate, or adapt for their context.
- **Student-friendly structure** — Units and subtopics match syllabus sections; language is kept clear for ages **16–18** and **ESL** learners.
- **Teacher contributions** — Issues and pull requests welcome for examples, exam-style questions, and local adaptations.
- **SDG 4** — Reduce barriers to quality CS education by sharing organised materials, contribution guides, and transparent roadmaps.

## What is inside

| Area | Description |
| --- | --- |
| [syllabus/syllabus.md](syllabus/syllabus.md) | Syllabus overview, aims, content map, assessment summary (derived from official syllabus text). |
| [syllabus/scheme_of_work.md](syllabus/scheme_of_work.md) | Scheme of Work cross-reference: guided hours, teaching order, key concepts. |
| [units/](units/) | Twenty units (`unit-01-…` through `unit-20-…`), each with `README.md` and `subtopics/*/notes.md`, `examples.md`, `exercises.md`. |
| [resources/](resources/) | `diagrams/`, `code/`, `references/originals/` (canonical PDF copies where permitted locally). |

Official PDFs included locally for convenience (see `resources/references/originals/`):

- Syllabus (2027–2029 series)
- Pseudocode Guide for Teachers (2027–2029 series)
- Scheme of Work and Learner Guide (2021 onwards)

## How to use this repo

### Students

1. Start from [syllabus/syllabus.md](syllabus/syllabus.md) to see how **Papers 1–4** map to topics.
2. Open the unit that matches your class order (your school may differ from the suggested order in the Scheme of Work).
3. For each subtopic, read **notes** → study **examples** → attempt **exercises**; check **Exam Tip** and **Common Mistakes** boxes.
4. Cross-check every statement against your **current exam series** syllabus PDF.

### Teachers

1. Use unit `README.md` files for **learning objectives** and **key terms** when planning lessons.
2. Align with [syllabus/scheme_of_work.md](syllabus/scheme_of_work.md) for **suggested hours** and **key concept** tags (KC1–KC5).
3. Contribute improvements via [CONTRIBUTING.md](CONTRIBUTING.md); use suggested labels in [.github/github-labels.md](.github/github-labels.md).

## Folder structure

```text
CS9618/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── roadmap.md
├── syllabus/
│   ├── syllabus.md
│   └── scheme_of_work.md
├── units/
│   ├── unit-01-information-representation/
│   │   ├── README.md
│   │   └── subtopics/
│   │       └── <subtopic>/
│   │           ├── notes.md
│   │           ├── examples.md
│   │           └── exercises.md
│   └── ...
├── resources/
│   ├── diagrams/
│   ├── code/
│   └── references/
└── .github/
    └── github-labels.md
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, content style, syllabus alignment, and licensing. See [roadmap.md](roadmap.md) for planned work.

To **regenerate** unit/subtopic skeletons after editing objectives metadata, run:

`python3 tools/generate_units.py`

## Recognition

Course structure and learning objectives follow **Cambridge International AS & A Level Computer Science 9618**. Community text and examples in this repository are MIT-licensed unless otherwise stated in a file.
