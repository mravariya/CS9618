# Cambridge CIE CS9618 Open Learning (SDG 4 Initiative)

World-class, **open-source** learning materials for **Cambridge International AS & A Level Computer Science (9618)**—structured for **conceptual depth**, **exam rigour**, **IB-style inquiry**, and **global collaboration**. This project supports **UN Sustainable Development Goal 4 (Quality Education)** by making syllabus-mapped modules, worked solutions, and optional **Manim** animations freely reusable and improvable.

> **Disclaimer:** Independent educational resource; **not** affiliated with Cambridge Assessment International Education. Verify all assessment details against your **official syllabus** and **School Support Hub**. Community Markdown and scripts are **MIT-licensed**; Cambridge PDFs in `resources/references/originals/` remain **their copyright**. See [LICENSE](LICENSE).

## Vision and mission

- **Teach deeply** — Layered explanations (intuition → formal → applied), misconceptions, and differentiation.
- **Pedagogy** — Pre-read, inquiry prompts, scaffolding, reflection; aligned with **9618** assessment objectives.
- **Visual learning** — Each subtopic includes an **animation plan**, `animation.md`, and `animations/scene.py` (Manim Community / 3b1b-style motion graphics).
- **Open collaboration** — Teachers and learners improve content via [CONTRIBUTING.md](CONTRIBUTING.md); labels in [.github/github-labels.md](.github/github-labels.md).

## Repository map

| Path | Role |
| --- | --- |
| [syllabus/syllabus.md](syllabus/syllabus.md) | Syllabus overview, papers, content grid |
| [syllabus/scheme_of_work.md](syllabus/scheme_of_work.md) | Guided hours, teaching order, KC1–KC5 |
| [units/](units/) | 20 units → 44 subtopics; each module has **notes**, **examples**, **exercises**, **solutions**, **animation** |
| [docs/animations-setup.md](docs/animations-setup.md) | FFmpeg, Cairo, `pip install manim`, troubleshooting |
| [tools/generate_units.py](tools/generate_units.py) | Curriculum metadata → base unit tree |
| [tools/generate_learning_modules.py](tools/generate_learning_modules.py) | Full pedagogical Markdown + Manim stubs |
| [tools/premium_topic_1_1.py](tools/premium_topic_1_1.py) | **Section 1.1** deep content + **7** Manim scenes |

### Subtopic folder layout

```text
units/.../subtopics/<subtopic-name>/
├── notes.md
├── examples.md
├── exercises.md
├── solutions.md
├── animation.md
└── animations/
    └── scene.py
```

**Topic 1.1 (Data Representation)** is intentionally the most detailed module (extended notes, multi-scene Manim).

## How to use (students)

1. Read [syllabus/syllabus.md](syllabus/syllabus.md) for **paper → topic** mapping.
2. Open a unit `README.md` (concept map + objectives + subtopic links).
3. Study each subtopic: **notes** → **examples** → **exercises** → **solutions**.
4. Optional: render **Manim** scenes listed in `animation.md`.

## How to use (teachers)

- Plan lessons from unit objectives and **Scheme of Work** hours in [syllabus/scheme_of_work.md](syllabus/scheme_of_work.md).
- Use **inquiry** and **differentiation** blocks in `notes.md` for starter/plenary.
- Assign **exercises.md**; use **solutions.md** for formative feedback.
- Contribute richer **Manim** scenes or local scenarios (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## How to run animations

1. Install system dependencies (FFmpeg; on macOS often Cairo + pkg-config). Full steps: [docs/animations-setup.md](docs/animations-setup.md).
2. `pip install -r requirements-animations.txt` (prefer a virtual environment).
3. From the subtopic directory:

```bash
manim -pql animations/scene.py <SceneName>
```

Example (Topic 1.1):

```bash
cd units/unit-01-information-representation/subtopics/data-representation
manim -pql animations/scene.py Topic11TitleCard
```

**Manim Community** (`pip install manim`) implements the `manim` CLI. The original [3b1b/manim](https://github.com/3b1b/manim) repository is the historical home of the project; APIs overlap for introductory scenes.

## Regenerating content (automation)

After editing curriculum data in `tools/generate_units.py`:

```bash
python3 tools/generate_units.py
python3 tools/generate_learning_modules.py
```

Section **1.1** premium text and scenes are merged from `tools/premium_topic_1_1.py` on each run.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [roadmap.md](roadmap.md).

## Recognition

Syllabus structure and learning outcomes follow **Cambridge International 9618**. Thank you to the open **Manim** community and educators who extend this repository.
