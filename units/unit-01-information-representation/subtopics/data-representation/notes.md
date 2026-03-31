# Data Representation (Syllabus 1.1)

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
