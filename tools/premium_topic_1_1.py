# Premium learning module exports for syllabus section 1.1 (data representation).
# Consumed by tools/generate_learning_modules.py

NOTES_MD = r"""# Data Representation (Syllabus 1.1)

**Syllabus:** Cambridge International AS & A Level Computer Science **9618** — **Section 1.1**  
**Module type:** Deep conceptual + exam technique + animation-ready storyboards.

---

## 1. Pre-read (activate prior knowledge)

You should already be comfortable with:

- **Whole numbers** in base 10 (denary): columns are powers of 10.
- The idea that **digits** are symbols and **value** depends on **position** (place value).
- **Fractions / negative numbers** as ideas (we will connect negatives to **two’s complement** later in this module).

*Quick check:* Expand 173 by place value: 1×100 + 7×10 + 3×1. That “expand by powers” habit is the same skill in binary and hexadecimal.

---

## 2. Inquiry / wonder questions (IB-style)

- If a wire can only be **high** or **low**, why did engineers standardise on **binary** rather than three or ten voltage levels?
- Why is **hexadecimal** “friendly” if computers are **binary**?
- When marketing says **“1 KB”**, what exactly is being counted—1000 bytes or 1024 bytes—and who cares?
- Why can adding two positive binary integers sometimes produce a **wrong signed** result in a fixed register width?

---

## 3. Learning objectives (syllabus-mapped)

- Understand **binary magnitudes** and the difference between **binary prefixes** (kibi, mebi, …) and **decimal/SI prefixes** (kilo, mega, …).
- Use **binary, denary, hexadecimal**, **BCD**, and **one’s/two’s complement**; **convert** between representations.
- Perform **binary addition and subtraction**; explain **overflow** for signed integers in fixed width.
- Describe practical applications of **BCD** and **hexadecimal**.
- Explain **character** data in binary form for **ASCII**, **extended ASCII**, and **Unicode** (no memorised code tables).

---

## 4. Key terms (definitions)

| Term | Definition |
| --- | --- |
| **Bit** | Binary digit: 0 or 1; smallest unit of information in classical digital logic. |
| **Byte** | Commonly 8 bits; a convenient chunk size for memory and files (historical standardisation). |
| **Denary (decimal)** | Base 10 representation using digits 0–9; everyday arithmetic. |
| **Binary** | Base 2 representation using digits 0 and 1; matches two-state devices. |
| **Hexadecimal** | Base 16, digits 0–9 and A–F; each hex digit maps cleanly to **four bits** (one **nibble**). |
| **BCD (Binary Coded Decimal)** | Each denary digit encoded separately (often 4 bits per digit); human-centric for numeric displays. |
| **One’s complement** | Flip all bits; historically used; asymmetric zero patterns in some widths. |
| **Two’s complement** | Dominant signed integer representation: flip bits then add 1 (to negative) in fixed width; one zero. |
| **Overflow** | Result cannot fit in available bits; interpretation depends on **unsigned vs signed** context. |
| **ASCII** | 7-bit character coding for basic English/control characters; foundation of many text systems. |
| **Extended ASCII** | 8-bit extensions / code pages; more symbols but **not** universal across systems. |
| **Unicode** | Universal character set with multiple **encoding forms** (e.g. UTF-8) for interchange. |
| **Kibi / Mebi / Gibi / Tebi** | IEC binary prefixes: 2^10, 2^20, 2^30, 2^40 multipliers. |
| **Kilo / Mega / Giga / Tera (SI)** | Decimal prefixes: 10^3, 10^6, 10^9, 10^12 when used in SI sense. |

---

## 5. Conceptual explanation (layered)

### 5.1 First principles (intuition)

**Digital hardware is noisy-thresholded into discrete states.** Two states are easier to separate reliably than many. That engineering fact pushes **binary** as the universal internal language.

**Representations are conventions.** The same 8 bits might mean an unsigned integer, a two’s complement integer, an ASCII character, or part of an audio sample—**metadata + program** decide the meaning.

### 5.2 Structured explanation (A-Level rigor)

**Place value** generalises: in base *b*, digit columns are powers of *b*. Converting denary → binary is repeated division by 2 (remainders are bits); binary → denary is sum of (bit × 2^position).

**Hexadecimal** groups binary into nibbles: 4 bits map to one hex digit. That reduces transcription errors for long patterns (memory addresses, dumps).

**BCD** trades storage efficiency for **digit-by-digit** fidelity to denary—useful when rounding in binary floating formats would be unacceptable for **exact decimal** business rules (also common in embedded displays).

**Two’s complement** encodes negatives so that addition/subtraction uses the **same hardware** as unsigned, with fixed width. The leftmost bit is the **sign bit** in the standard interpretation.

**Overflow (signed, two’s complement):** if two positives add to a negative pattern, or two negatives add to a positive pattern, the **mathematical** result is outside the representable range for that bit width.

### 5.3 Analogies and real-world hooks

- **Odometer / cyclometer:** Fixed digits “roll over” like **unsigned overflow**—the pattern repeats with a modulus.
- **Thermometer scale:** Choosing a signed representation is like agreeing whether “all 1s” means “very cold” or “error flag”—**context** matters.
- **Shipping container vs pallet:** **Hex** is a bigger “chunk label” than raw bits—like reading container codes instead of every nail.

---

## 6. Visual explanation plan (for animation)

Linked artefacts:

- [animation.md](animation.md)
- `animations/scene.py`

**Storyboard:**

1. **Title:** position 1.1 as the foundation for everything else in CS (all data → bits).
2. **Why binary:** two stable states → reliable storage and transmission.
3. **Powers of two:** place-value columns for bits; relate to memory sizing.
4. **Kibi vs Kilo:** side-by-side numbers (1024 vs 1000) to motivate IEC vs SI.
5. **Hex bridge:** show a byte split into two nibbles → two hex digits.
6. **Two’s complement:** small negative example on a number line / bit flip + add 1 choreography.
7. **Unicode mosaic:** “many scripts, one interchange mission” (no memorisation).

---

## 7. Manim animation script

Implemented in **`animations/scene.py`**.

```bash
manim -pql animations/scene.py Topic11TitleCard
manim -pql animations/scene.py WhyBinaryScene
# … see animation.md for full scene list
```

---

## 8. Guided examples

See [examples.md](examples.md).

---

## 9. Practice prompts (scaffolded)

See [exercises.md](exercises.md).

---

## 10. Solutions

See [solutions.md](solutions.md).

---

## 11. Exam-style questions (Cambridge format)

See [exercises.md](exercises.md), section **Exam-style**.

---

## 12. Differentiation

### Support

- Learn **4-bit binary → hex** first (0–F table), then expand to bytes.
- Use a **fixed width** (e.g. 8 bits) for all signed examples until patterns stabilise.

### Extension

- Prove why two’s complement addition matches integer addition modulo 2^n.
- Compare **UTF-8** (variable width) vs **UTF-16** for storage and streaming trade-offs (syllabus: know Unicode exists; extension for university prep).

---

## 13. Common misconceptions

- **“Hex is a different number system computers use.”** Computers store **bits**; hex is a **human** view.
- **“Two’s complement is a different operation from addition.”** Same adder; **interpretation** of MSB makes it signed.
- **“Overflow always means an error.”** Unsigned wrap-around can be intentional (e.g. timers); **signed overflow** in arithmetic is usually a bug unless designed for.

---

## 14. Summary notes

- Master **conversions** and show **working**.
- Be precise about **prefixes** (IEC vs SI) and **context** (signed vs unsigned).
- For characters: **ASCII vs extended ASCII vs Unicode** roles, not memorised codes.

---

## 15. Reflection questions

- Which representation will you practise **daily** for the next week?
- Where in a computer system might **the same bytes** mean different things?
- What is one **exam-style** “explain” question you would write for a peer?

---

**SDG 4:** If this helped you learn, consider contributing fixes or translations via [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
"""

EXAMPLES_MD = r"""# Guided examples — Data Representation (1.1)

---

## Example 1 — Denary to binary (unsigned, 8-bit)

**Task:** Convert denary **205** to an 8-bit binary pattern.

**Working (division by 2, remainders least significant first):**

205 ÷ 2 = 102 r **1**  
102 ÷ 2 = 51 r **0**  
51 ÷ 2 = 25 r **1**  
25 ÷ 2 = 12 r **1**  
12 ÷ 2 = 6 r **0**  
6 ÷ 2 = 3 r **0**  
3 ÷ 2 = 1 r **1**  
1 ÷ 2 = 0 r **1**

Read remainders from bottom to top: **11001101**

**Check:** 128 + 64 + 8 + 4 + 1 = 205. ✓

---

## Example 2 — Binary to hexadecimal

**Task:** `11001101` → hex.

**Working:** Split into nibbles from the right: `1100` `1101`  
`1100` = 12 → **C**  
`1101` = 13 → **D**  
Result: **0xCD** (exam style may write **CD₁₆** or `&CD` in assembly contexts).

---

## Example 3 — Two’s complement, 8-bit: represent −42

**Method:** Positive 42 in 8 bits is `00101010`. Invert → `11010101`. Add 1 → `11010110`.

**Check idea:** Add `00101010` + `11010110` = `1 00000000` → discard carry out → `00000000`.

---

## Example 4 — Prefix comparison (KiB vs KB)

**Statement:** “Download speed 100 MB/s” vs “file size 100 MiB.”

**Explain:** **MB** often uses decimal 10^6 in networking/marketing; **MiB** is 2^20 bytes by IEC definition. Close in wording, different magnitudes—precision matters in exams when comparing storage vs transfer claims.

---

## Example 5 — BCD vs pure binary for denary 39

- **Unsigned 8-bit binary:** `00100111` (one byte, value 39)
- **BCD (two digits):** `0011` `1001` (nibble 3, nibble 9)

**Justify BCD:** easier mapping to **seven-segment** / decimal business rules; **cost:** less compact than binary integer encoding.

💡 **Exam Tip:** When asked to **justify**, always give **criteria** (accuracy, hardware, human factors, storage).

🔗 **Further Reading:** Official syllabus PDF in `resources/references/originals/`
"""

EXERCISES_MD = r"""# Practice — Data Representation (1.1)

---

## A. Short answer

1. **State** the numeric multiplier for **1 GiB** in bytes as a power of two.
2. **State** the numeric multiplier for **1 GB** in the SI decimal sense (bytes) as a power of ten.
3. **Define** **two’s complement** in one sentence for a fixed-width integer.

## B. Structured (show working)

1. Convert denary **91** to **8-bit binary**.
2. Convert binary **`01001110`** to **denary** (unsigned interpretation).
3. Convert binary **`01001110`** to **hexadecimal**.
4. Using **8-bit two’s complement**, represent denary **−96**.

## C. Exam-style

1. **Explain** how **overflow** can occur when two **positive** 8-bit two’s complement integers are added.
2. **Describe** a practical situation where **BCD** might be preferred to a plain binary integer encoding.
3. **Justify** using **hexadecimal** when debugging memory contents instead of displaying raw binary.

## D. Scenario

A media app reports “**500 MB** free” but the OS reports “**476.8 MiB** free” for the same partition.

- **Identify** two different interpretations of **mega/mebi** that could cause confusion.
- **Explain** why developers should document which interpretation their UI uses.

---

_Original questions — not copied from Cambridge past papers._
"""

SOLUTIONS_MD = r"""# Solutions — Data Representation (1.1)

## A. Short answer

1. **1 GiB** = 2^30 bytes (= 1 073 741 824 bytes).
2. **1 GB** (SI, decimal) = 10^9 bytes (= 1 000 000 000 bytes) when used in that sense.
3. **Two’s complement:** fixed-width signed encoding where negatives are formed by **inverting bits and adding 1** (modulo 2^n), so subtraction can reuse addition hardware.

## B. Structured

1. **91** = 64 + 16 + 8 + 2 + 1 → **`01011011`**.
2. Unsigned: 64 + 8 + 4 + 2 = **78**.
3. Nibbles `0100` `1110` → **4E** (hex).
4. **−96:** +96 = `01100000`; invert → `10011111`; +1 → **`10100000`** (8-bit two’s complement).

## C. Exam-style (model reasoning)

1. **Explain overflow:** If the true sum ≥ 2^(n−1) for the positive range, the bit pattern becomes the **sign bit = 1**, i.e. looks **negative** in two’s complement → inconsistent with “two positives” expectation → overflow.
2. **BCD situation:** when **exact decimal digit** fidelity matters (e.g. currency step of 0.01 in some embedded/legacy designs) or **direct drive** of decimal displays—accept answers referencing rounding in binary integer/float.
3. **Justify hex:** fewer symbols than binary → fewer transcription errors; maps cleanly to **nibbles** and **byte-aligned** memory views.

## D. Scenario

- **Interpretations:** 10^6 bytes per “MB” vs 2^20 bytes per “MiB” (or ambiguous “MB”).
- **Documentation:** prevents user mistrust, support tickets, and data loss when users estimate downloads/backups.

---

Cross-check methods with your teacher against the **current** 9618 syllabus for your series.
"""

ANIMATION_MD = r"""# Animation — Data Representation (1.1)

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

From this folder (`.../data-representation/`):

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
"""

SCENE_PY = r'''"""
CS9618 — Section 1.1 Data Representation
Manim Community scenes (3Blue1Brown-style pedagogy).

Render examples:
    manim -pql animations/scene.py Topic11TitleCard
    manim -pql animations/scene.py WhyBinaryScene
"""
from manim import BLUE, DOWN, GREEN, LEFT, ORANGE, RIGHT, UP, FadeIn, FadeOut, Scene, Text, VGroup


class Topic11TitleCard(Scene):
    def construct(self):
        t1 = Text("Cambridge 9618 — 1.1", font_size=36)
        t2 = Text("Data Representation", font_size=52)
        sub = Text("Bits, bases, prefixes, signed integers, characters", font_size=22)
        grp = VGroup(t1, t2, sub).arrange(DOWN, buff=0.35)
        self.play(FadeIn(grp, shift=0.2 * DOWN))
        self.wait(2.5)
        self.play(FadeOut(grp))


class WhyBinaryScene(Scene):
    def construct(self):
        title = Text("Why binary?", font_size=40).to_edge(UP)
        self.play(FadeIn(title))
        hi = Text("HIGH", font_size=32, color=GREEN)
        lo = Text("LOW", font_size=32, color=BLUE)
        lo.shift(2 * LEFT)
        hi.shift(2 * RIGHT)
        gap = Text("clear gap → reliable detection", font_size=22).next_to(VGroup(lo, hi), DOWN, buff=0.8)
        self.play(FadeIn(lo), FadeIn(hi))
        self.play(FadeIn(gap))
        self.wait(2)
        bridge = Text("Two states → one bit (0 or 1)", font_size=28).next_to(gap, DOWN, buff=0.6)
        self.play(FadeIn(bridge))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, lo, hi, gap, bridge)))


class PowersOfTwoNumberLine(Scene):
    def construct(self):
        title = Text("Place value: powers of two (8 bits)", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        labels = []
        for i in range(8):
            val = 2 ** (7 - i)
            bit_pos = f"bit{7 - i}"
            labels.append(Text(f"{bit_pos}: 2^{7 - i} = {val}", font_size=20))
        col = VGroup(*labels).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        col.next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(col, lag_ratio=0.15))
        self.wait(2)
        hint = Text("Add selected powers → unsigned denary value", font_size=22, color=ORANGE)
        hint.next_to(col, DOWN, buff=0.5)
        self.play(FadeIn(hint))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, col, hint)))


class KibiVsKiloComparison(Scene):
    def construct(self):
        title = Text("Kibi vs kilo (know both stories)", font_size=34).to_edge(UP)
        self.play(FadeIn(title))
        left = VGroup(
            Text("IEC binary", font_size=28),
            Text("1 KiB = 1024 B", font_size=24),
            Text("1 MiB = 1024 KiB", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT).shift(2.2 * LEFT)
        right = VGroup(
            Text("SI / decimal", font_size=28),
            Text("1 kB = 1000 B", font_size=24),
            Text("(when used that way)", font_size=20, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT).shift(2.2 * RIGHT)
        self.play(FadeIn(left), FadeIn(right))
        mid = Text("Close words, different counts", font_size=26).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(mid))
        self.wait(2.5)
        exam = Text("Examiners reward precise terminology", font_size=22).to_edge(DOWN)
        self.play(FadeIn(exam))
        self.wait(2)
        self.play(FadeOut(VGroup(title, left, right, mid, exam)))


class HexNibbleBridge(Scene):
    def construct(self):
        title = Text("One byte ↔ two hex digits", font_size=34).to_edge(UP)
        self.play(FadeIn(title))
        byte_txt = Text("11001101", font_size=36)
        n1 = Text("1100", font_size=32, color=BLUE).next_to(byte_txt, UP, buff=0.8)
        n2 = Text("1101", font_size=32, color=GREEN).next_to(byte_txt, UP, buff=0.8)
        # position nibbles above left/right halves — simplified layout
        n1.shift(1.8 * LEFT)
        n2.shift(1.8 * RIGHT)
        h1 = Text("C", font_size=40, color=BLUE).next_to(n1, UP, buff=0.3)
        h2 = Text("D", font_size=40, color=GREEN).next_to(n2, UP, buff=0.3)
        self.play(FadeIn(byte_txt))
        self.play(FadeIn(VGroup(n1, n2)))
        self.play(FadeIn(VGroup(h1, h2)))
        arrow = Text("4 bits = 1 hex digit (nibble)", font_size=22).to_edge(DOWN)
        self.play(FadeIn(arrow))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, byte_txt, n1, n2, h1, h2, arrow)))


class TwosComplementStory(Scene):
    def construct(self):
        title = Text("Two's complement (8-bit sketch)", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        p = Text("+42  →  00101010", font_size=28)
        inv = Text("invert → 11010101", font_size=26, color=ORANGE)
        add1 = Text("+1   →  11010110   (= −42)", font_size=28, color=GREEN)
        grp = VGroup(p, inv, add1).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        grp.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(p))
        self.play(FadeIn(inv))
        self.play(FadeIn(add1))
        note = Text("Same adder hardware; MSB is sign bit", font_size=22).next_to(grp, DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(3)
        self.play(FadeOut(VGroup(title, grp, note)))


class UnicodeMosaic(Scene):
    def construct(self):
        title = Text("Characters need agreed standards", font_size=32).to_edge(UP)
        self.play(FadeIn(title))
        samples = VGroup(
            Text("ASCII — foundational English/control", font_size=22),
            Text("Extended ASCII — code pages (limited)", font_size=22),
            Text("Unicode — universal repertoire + UTF-8/16…", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        samples.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.3)
        self.play(FadeIn(samples, lag_ratio=0.2))
        tail = Text("Syllabus: concepts, not memorising code tables", font_size=22, color=ORANGE).to_edge(DOWN)
        self.play(FadeIn(tail))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, samples, tail)))
'''
