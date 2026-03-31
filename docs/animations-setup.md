# Manim setup (optional)

Animations use **[Manim Community](https://www.manim.community/)** (`pip install manim`), the maintained distribution with the `manim` CLI. Grant Sanderson’s original project is [github.com/3b1b/manim](https://github.com/3b1b/manim); scene code here uses the Community import style (`from manim import …`).

## System dependencies

Manim needs **FFmpeg** on your `PATH`. On many systems you also need **Cairo**, **pkg-config**, and related build tools so `pycairo` can compile.

### macOS (Homebrew example)

```bash
brew install ffmpeg pkg-config cairo
```

Then create a virtual environment and install Python packages:

```bash
python3 -m venv .venv_manim
source .venv_manim/bin/activate   # Windows: .venv_manim\Scripts\activate
pip install -r requirements-animations.txt
```

### Linux

Use your distribution’s packages for `ffmpeg`, `libcairo2-dev`, `pkg-config`, and a C compiler, then `pip install -r requirements-animations.txt`.

### Windows

Install FFmpeg, Visual C++ Build Tools, and Cairo as described in the [Manim Community installation guide](https://docs.manim.community/en/stable/installation.html).

## Render a scene

From a subtopic directory (example: Topic 1.1):

```bash
cd units/unit-01-information-representation/subtopics/data-representation
manim -pql animations/scene.py Topic11TitleCard
```

- `-ql` — quick / low quality (fast preview)  
- `-p` — preview when supported  

Output is written under `media/videos/` relative to the current working directory.

## Troubleshooting

If `pip install manim` fails on **pycairo**, install system Cairo and **pkg-config** first, then retry in a clean venv.
