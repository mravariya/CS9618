# Animation — Data Representation (1.1)

## Purpose

High-quality **motion graphics** for intuition: why binary, how place value scales, why IEC prefixes exist, how hex maps to nibbles, how two’s complement behaves, and how Unicode fits the “characters as bits” story.

## Concepts visualised

| Scene class | Teaching focus |
| --- | --- |
| `Topic11TitleCard` | Module title + one-sentence mission |
| `WhyBinaryScene` | Reliable discrimination of two states |
| `PowersOfTwoNumberLine` | Place value columns 2^0 … 2^7 |
| `KibiVsKiloComparison` | 1024 vs 1000 mental model |
| `HexNibbleBridge` | Byte → two hex digits |
| `TwosComplementStory` | Flip + 1 choreography for a small negative |
| `UnicodeMosaic` | Diversity of characters / encodings (conceptual) |

## Prerequisites

- Python **3.10+** recommended  
- **FFmpeg** on your PATH  
- From repo root: `pip install -r requirements-animations.txt`

## Render

From this folder (`.../1.1-data-representation/`):

```bash
manim -pql animations/scene.py Topic11TitleCard
manim -pql animations/scene.py WhyBinaryScene
manim -pql animations/scene.py PowersOfTwoNumberLine
manim -pql animations/scene.py KibiVsKiloComparison
manim -pql animations/scene.py HexNibbleBridge
manim -pql animations/scene.py TwosComplementStory
manim -pql animations/scene.py UnicodeMosaic
```

## Expected output

Renders under `media/videos/<quality>/animations/<scene_id>/` relative to where you run the command.

## Note on Manim editions

This repo uses **Manim Community** (`pip install manim`). Grant Sanderson’s original code is at [github.com/3b1b/manim](https://github.com/3b1b/manim); APIs overlap for introductory scenes.

## Contributing

See [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
