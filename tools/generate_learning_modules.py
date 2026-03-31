#!/usr/bin/env python3
"""
Generate full learning modules: notes, examples, exercises, solutions, animation.md,
and animations/scene.py for every CS9618 subtopic.

Topic 1.1 (data-representation) uses premium content from tools.premium_topic_1_1.
Run from repo root:  python3 tools/generate_learning_modules.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_units import OBJECTIVES, UNITS  # noqa: E402

UNITS_DIR = ROOT / "units"


def slug_to_class_base(folder: str) -> str:
    """Strip leading syllabus label (e.g. 1.1-) for valid Python class names."""
    folder = re.sub(r"^\d+\.\d+-", "", folder)
    parts = re.split(r"[-_]+", folder)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def section_from_folder(folder: str) -> str:
    m = re.match(r"^(\d+)\.(\d+)-", folder)
    return f"Section {m.group(1)}.{m.group(2)}" if m else "See syllabus/syllabus.md"


def concept_map_ascii(unit_title: str, subtopics: list[tuple[str, str, str]]) -> str:
    lines = [
        f"                    +----------------------+",
        f"                    |   {unit_title[:18]:<18}   |",
        f"                    +----------+-----------+",
    ]
    for _folder, t, _k in subtopics:
        short = t[:22] + ("…" if len(t) > 22 else "")
        lines.append(f"                            |")
        lines.append(f"                     +-----v-----+")
        lines.append(f"                     | {short:<21} |")
        lines.append(f"                     +-----------+")
    return "\n".join(lines)


def unit_readme_enhanced(u: dict) -> str:
    sub_links = "\n".join(
        f"- **{t}** — [notes](subtopics/{folder}/notes.md) · [examples](subtopics/{folder}/examples.md) · "
        f"[exercises](subtopics/{folder}/exercises.md) · [solutions](subtopics/{folder}/solutions.md) · "
        f"[animation](subtopics/{folder}/animation.md) · `animations/scene.py`"
        for folder, t, _ in u["subtopics"]
    )
    sow = u["sow_order"]
    sow_line = (
        f"- **Scheme of Work:** suggested **{u['sow_hours']}** guided hours; teaching order **{sow}**."
        if sow
        else f"- **Scheme of Work:** **{u['sow_hours']}** guided hours; integrate **continuously** across the course."
    )
    kc = ", ".join(u["kc"])
    terms = ", ".join(f"`{t}`" for t in u["key_terms"])
    apps = "\n".join(f"- {a}" for a in u["applications"])
    objectives = []
    for _folder, _st, obj_key in u["subtopics"]:
        for line in OBJECTIVES.get(obj_key, []):
            objectives.append(f"- {line}")
    obj_block = "\n".join(objectives)
    cmap = concept_map_ascii(u["title"], u["subtopics"])

    return dedent(
        f"""\
        # {u["title"]}

        **Level:** {u["level"]} · **Primary assessment:** {u["paper"]}  
        **Key concepts (Scheme of Work):** {kc}

        ## Overview

        {u["overview"]}

        ## Concept map (text)

        ```text
        {cmap}
        ```

        ## Learning objectives (syllabus-mapped)

        {obj_block}

        {sow_line}

        ## Key terms

        {terms}

        ## Real-world applications

        {apps}

        ## Subtopics (full modules)

        {sub_links}

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
        """
    ).strip() + "\n"


def glossary_from_terms(terms: list[str]) -> str:
    rows = ["| Term | Working definition (for study) |", "| --- | --- |"]
    fallback = (
        "Relates to this unit; define using your own words and the official syllabus."
    )
    hints: dict[str, str] = {
        "binary": "Number base 2; digits 0 and 1; matches on/off in hardware.",
        "hexadecimal": "Base 16; uses 0–9 and A–F; compact shorthand for binary nibbles.",
    }
    for t in terms:
        rows.append(f"| **{t}** | {hints.get(t.lower(), fallback)} |")
    return "\n".join(rows)


def write_notes_full(
    unit_title: str,
    sub_title: str,
    obj_key: str,
    syllabus_section: str,
    key_terms: list[str],
) -> str:
    objs = OBJECTIVES.get(obj_key, ["Follow the official syllabus for this subtopic."])
    obj_bullets = "\n".join(f"- {o}" for o in objs)
    glossary = glossary_from_terms(key_terms[:12])
    rel_anim = f"See [animation.md](animation.md) and render scenes in `animations/scene.py`."

    return dedent(
        f"""\
        # {sub_title}

        **Syllabus:** Cambridge International AS & A Level Computer Science **9618** ({syllabus_section})  
        **Module type:** Inquiry-led, ESL-friendly, exam-aligned.

        ---

        ## 1. Pre-read (activate prior knowledge)

        Before you start, make sure you can:

        - Explain in one sentence what a **computer** stores at the lowest level (bits / states).
        - Read a small **whole number** in everyday base 10 (denary).
        - Follow a short **step-by-step** procedure without skipping lines (habit for traces and algorithms).

        _If any item feels hard, skim the Support section first._

        ---

        ## 2. Inquiry / wonder questions (IB-style)

        - Where do **patterns** appear in how we represent information?
        - Why might humans use **different bases** or encodings if computers only use **two states**?
        - What could go wrong if two systems **interpret the same bits differently**?
        - When is **compactness** more important than **human readability**?

        ---

        ## 3. Learning objectives (syllabus-mapped)

        {obj_bullets}

        ---

        ## 4. Key terms (definitions)

        {glossary}

        ---

        ## 5. Conceptual explanation (layered)

        ### 5.1 First principles (intuition)

        This subtopic sits inside **{unit_title}**. At 9618 level, examiners reward **precise vocabulary** tied to **short explanations**. Start from a concrete picture (a device, a file, a wire), then name the abstract idea.

        ### 5.2 Structured explanation (A-Level rigor)

        Work through each objective above as a **checklist**. For every bullet, you should be able to: **define** the idea, **give an example**, and **state one limitation or assumption**.

        ### 5.3 Analogies and real-world hooks

        - **Map / recipe:** A representation is like agreeing whether “3” means cups, litres, or millilitres—same symbol, different interpretation unless we share a **standard**.
        - **Postal system:** Protocols for mail parallel **rules for bits**: format, addressing, and meaning must align at both ends.

        ---

        ## 6. Visual explanation plan (for animation)

        {rel_anim}

        Storyboard (adapt in `scene.py`):

        1. Title + one-sentence “why this matters”.
        2. **Zoom in** from real device → bits / symbols used in this subtopic.
        3. **Transform** step-by-step (e.g. relabel, reorder, highlight) rather than a wall of text.
        4. **Checkpoint** slide: three keywords to remember.

        ---

        ## 7. Manim animation script

        Implemented in **`animations/scene.py`**. Render with Manim Community:

        `manim -pql animations/scene.py <SceneName>`

        ---

        ## 8. Guided examples

        Work through [examples.md](examples.md) before the practice set.

        ---

        ## 9. Practice prompts (scaffolded)

        See [exercises.md](exercises.md) (moves from short recall → structured → exam-style).

        ---

        ## 10. Solutions

        Full worked answers: [solutions.md](solutions.md).

        ---

        ## 11. Exam-style questions (Cambridge format)

        Located in [exercises.md](exercises.md) (section **Exam-style**). Use **command words** exactly as asked.

        ---

        ## 12. Differentiation

        ### Support (simplified)

        - Read objectives one at a time; for each, write **one** sentence in your own words.
        - Make a **mini-glossary** on an index card.

        ### Extension (challenge)

        - Link this subtopic to **another syllabus section** (e.g. hardware, security, databases).
        - Write a **compare/contrast** table for two methods or terms that are easily confused.

        ---

        ## 13. Common misconceptions

        - Mixing **representation** (how bits are interpreted) with **compression** or **encryption** (different purposes).
        - Using **informal** units (e.g. “kilo = 1024”) in contexts that require **IEC binary prefixes** (kibi, mebi, …) or **SI** clarity.
        - Answering **“what”** when the question asks **“why”** or **“justify”**.

        ---

        ## 14. Summary notes

        - Master the **definitions** in section 4.
        - Be able to **explain** each learning objective with an **example**.
        - Practise **exam technique**: label diagrams, show **working**, use **syllabus terms**.

        ---

        ## 15. Reflection questions

        - Which objective felt **easiest**? Why?
        - Which objective will you **revisit** tomorrow?
        - What is one **question** you would ask a teacher after reading this module?

        ---

        **SDG 4:** Quality education — share improvements via this repo’s [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
        """
    ).strip() + "\n"


def write_examples_layered(unit_title: str, sub_title: str, obj_key: str) -> str:
    return dedent(
        f"""\
        # Guided examples — {sub_title}

        Worked originals (not from past papers). Increase difficulty top → bottom.

        ---

        ## Example A — Recall (foundation)

        **Question:** Name two reasons teachers use **layered explanations** when introducing a technical topic.

        **Solution sketch:** (1) Builds shared vocabulary first. (2) Reduces cognitive load before abstract formalism.

        ---

        ## Example B — Application (scenario)

        **Question:** A learner says: “Hexadecimal is just for colours.” **Explain** why that is incomplete for 9618.

        **Solution sketch:** Hex is a **compact human view** of binary patterns; it appears in **memory addresses**, **machine-level dumps**, and **colour**—the syllabus expects **general** use, not one domain.

        ---

        ## Example C — Integration (exam-style stem)

        **Question:** **Describe** how **mis-matched interpretation** of stored bits could affect **data integrity** in a multi-system workflow.

        **Solution sketch:** Same bit pattern interpreted as different types/endianness/encodings → wrong values, corrupted fields, failed validation; mitigations include standards, metadata, agreed schemas.

        ---

        ## Example D — {unit_title} linkage

        **Question:** Link **one idea** from `{sub_title}` to another objective in **{unit_title}**.

        **Solution sketch:** Student selects a valid pairing and explains a **causal** or **dependency** relationship in 3–5 sentences.

        💡 **Exam Tip:** When a question says **justify**, include **evidence** and **criteria** (what you optimised for).

        🔗 Use objectives listed in [notes.md](notes.md) as a mark scheme for self-checking.
        """
    ).strip() + "\n"


def write_exercises_scaffolded(sub_title: str, _obj_key: str) -> str:
    return dedent(
        f"""\
        # Practice — {sub_title}

        ## Short answer

        1. **State** the main focus of `{sub_title}` in one sentence.
        2. **Identify** two syllabus terms you would use in an answer about this subtopic.
        3. **Give** one **advantage** and one **limitation** of a method discussed in this subtopic (choose a sensible method).

        ## Structured questions

        1. **Outline** a 3-step teaching sequence you would use to explain this subtopic to a peer.
        2. **Explain** why **precision of terminology** matters in Computer Science exams.
        3. **Compare** two related ideas from this subtopic (similarities + differences).

        ## Exam-style (Cambridge command words)

        1. **Define** … (insert a term from this subtopic).
        2. **Describe** … (insert a process or representation).
        3. **Explain** … (cause → consequence, with a concrete example).

        ## Scenario

        A school migrates systems. Give **two risks** and **two controls** relevant to `{sub_title}`.

        ---

        _Teachers:_ add local scenarios; do not paste copyrighted exam questions.
        """
    ).strip() + "\n"


def write_solutions_template(sub_title: str) -> str:
    return dedent(
        f"""\
        # Solutions — {sub_title}

        Model answers (abbreviated where obvious). In exams, expand with **context** from the question stem.

        ## Short answer

        1. **Sample:** Focus is defined by the syllabus objectives for this subtopic (see [notes.md](notes.md)).
        2. **Sample:** Any two correct terms from the subtopic glossary.
        3. **Sample:** Advantage + limitation must be **paired** with **because** and a **scenario**.

        ## Structured

        1. **Sample sequence:** hook → define terms → worked example → quick check question.
        2. **Sample:** terminology reduces ambiguity; enables **AO1/AO2** discrimination; supports peer review.
        3. **Sample:** two-column comparison; each row has **both** sides.

        ## Exam-style

        1–3. **Use** the definitions and explanations from [notes.md](notes.md); add **one sentence** linking to the stem.

        ## Scenario

        **Sample:** risk: misconfiguration / training gap / inconsistent standards; control: validation, access rights, testing, documentation.

        ---

        If your teacher’s mark scheme differs, follow the **official** guidance for your series.
        """
    ).strip() + "\n"


def write_animation_md(sub_title: str, _obj_key: str, scene_names: list[str]) -> str:
    scenes = "\n".join(f"- `{n}`" for n in scene_names)
    return dedent(
        f"""\
        # Animation — {sub_title}

        ## Purpose

        Visual, step-by-step intuition for **{sub_title}** (Cambridge 9618). Animations complement text—they do not replace the **syllabus** or **pseudocode guide**.

        ## Concepts visualised

        {scenes}

        ## Prerequisites

        - Python 3.10+ recommended
        - [FFmpeg](https://ffmpeg.org/) installed and on your `PATH`
        - `pip install -r requirements-animations.txt` (from repository root)

        ## Render (low quality, fast preview)

        From this subtopic folder:

        ```bash
        manim -pql animations/scene.py <SceneName>
        ```

        Example:

        ```bash
        manim -pql animations/scene.py {scene_names[0]}
        ```

        ## Expected output

        Manim writes rendered media under `media/videos/...` relative to the working directory. `-p` opens a preview when possible; `-ql` uses 480p for speed.

        ## 3b1b / Manim Community note

        This repo targets **Manim Community** (`pip install manim`), the actively maintained fork with the `manim` CLI. Grant Sanderson’s original repository is [3b1b/manim](https://github.com/3b1b/manim); APIs are similar for basic scenes.

        ## Contributing animations

        Keep scenes **short**, **readable**, and **syllabus-faithful**. See [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
        """
    ).strip() + "\n"


def generic_scene_py(folder: str, sub_title: str, objectives: list[str]) -> str:
    base = slug_to_class_base(folder)
    primary = f"{base}ModuleOverview"
    safe_title = sub_title.replace('"', "'")[:70]
    assigns = []
    for i, obj in enumerate(objectives[:7]):
        safe = json.dumps(obj[:100])
        assigns.append(f"        t{i} = Text({safe}, font_size=20, line_spacing=1.1)")
    if not assigns:
        assigns.append('        t0 = Text("CS9618 topic overview", font_size=28)')
    assign_block = "\n".join(assigns)
    tnames = ", ".join(f"t{i}" for i in range(len(assigns)))
    doc = f'''"""
Manim scenes for: {sub_title}
Subtopic folder: {folder}
Render: manim -pql animations/scene.py {primary}
"""
from manim import DOWN, LEFT, UP, FadeIn, Scene, Text, VGroup


class {primary}(Scene):
    def construct(self):
        title = Text({json.dumps(safe_title)}, font_size=32)
        title.to_edge(UP)
        self.play(FadeIn(title))
{assign_block}
        grp = VGroup({tnames}).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.4)
        self.play(FadeIn(grp, shift=0.1 * DOWN))
        self.wait(2)
'''
    return doc


def premium_1_1() -> None:
    try:
        from premium_topic_1_1 import (
            ANIMATION_MD,
            EXAMPLES_MD,
            EXERCISES_MD,
            NOTES_MD,
            SCENE_PY,
            SOLUTIONS_MD,
        )
    except ImportError:
        return
    base = (
        UNITS_DIR
        / "unit-01-information-representation"
        / "subtopics"
        / "1.1-data-representation"
    )
    base.mkdir(parents=True, exist_ok=True)
    (base / "notes.md").write_text(NOTES_MD, encoding="utf-8")
    (base / "examples.md").write_text(EXAMPLES_MD, encoding="utf-8")
    (base / "exercises.md").write_text(EXERCISES_MD, encoding="utf-8")
    (base / "solutions.md").write_text(SOLUTIONS_MD, encoding="utf-8")
    (base / "animation.md").write_text(ANIMATION_MD, encoding="utf-8")
    anim = base / "animations"
    anim.mkdir(parents=True, exist_ok=True)
    (anim / "scene.py").write_text(SCENE_PY, encoding="utf-8")


def scene_names_for(obj_key: str, folder: str) -> list[str]:
    if obj_key == "data-representation":
        return [
            "Topic11TitleCard",
            "WhyBinaryScene",
            "PowersOfTwoNumberLine",
            "KibiVsKiloComparison",
            "HexNibbleBridge",
            "TwosComplementStory",
            "UnicodeMosaic",
        ]
    base = slug_to_class_base(folder)
    return [f"{base}ModuleOverview"]


def main() -> None:
    for u in UNITS:
        udir = UNITS_DIR / u["folder"]
        udir.mkdir(parents=True, exist_ok=True)
        (udir / "README.md").write_text(unit_readme_enhanced(u), encoding="utf-8")
        terms = u["key_terms"]
        for folder, stitle, obj_key in u["subtopics"]:
            if obj_key == "data-representation":
                continue  # premium pass
            sdir = udir / "subtopics" / folder
            sdir.mkdir(parents=True, exist_ok=True)
            sec = section_from_folder(folder)
            (sdir / "notes.md").write_text(
                write_notes_full(u["title"], stitle, obj_key, sec, terms),
                encoding="utf-8",
            )
            (sdir / "examples.md").write_text(
                write_examples_layered(u["title"], stitle, obj_key),
                encoding="utf-8",
            )
            (sdir / "exercises.md").write_text(
                write_exercises_scaffolded(stitle, obj_key),
                encoding="utf-8",
            )
            (sdir / "solutions.md").write_text(
                write_solutions_template(stitle),
                encoding="utf-8",
            )
            names = scene_names_for(obj_key, folder)
            (sdir / "animation.md").write_text(
                write_animation_md(stitle, obj_key, names),
                encoding="utf-8",
            )
            anim = sdir / "animations"
            anim.mkdir(parents=True, exist_ok=True)
            objs = OBJECTIVES.get(obj_key, ["Follow the official syllabus for this subtopic."])
            (anim / "scene.py").write_text(
                generic_scene_py(folder, stitle, objs),
                encoding="utf-8",
            )

    premium_1_1()
    print("Learning modules generated (including premium 1.1 if premium_topic_1_1 present).")


if __name__ == "__main__":
    main()
