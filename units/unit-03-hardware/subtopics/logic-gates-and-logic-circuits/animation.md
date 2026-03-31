# Animation — Logic Gates and Logic Circuits

## Purpose

Visual, step-by-step intuition for **Logic Gates and Logic Circuits** (Cambridge 9618). Animations complement text—they do not replace the **syllabus** or **pseudocode guide**.

## Concepts visualised

- `LogicGatesAndLogicCircuitsModuleOverview`

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
manim -pql animations/scene.py LogicGatesAndLogicCircuitsModuleOverview
```

## Expected output

Manim writes rendered media under `media/videos/...` relative to the working directory. `-p` opens a preview when possible; `-ql` uses 480p for speed.

## 3b1b / Manim Community note

This repo targets **Manim Community** (`pip install manim`), the actively maintained fork with the `manim` CLI. Grant Sanderson’s original repository is [3b1b/manim](https://github.com/3b1b/manim); APIs are similar for basic scenes.

## Contributing animations

Keep scenes **short**, **readable**, and **syllabus-faithful**. See [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
