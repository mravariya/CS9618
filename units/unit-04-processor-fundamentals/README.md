# Processor Fundamentals

        **Level:** AS Level · **Primary assessment:** Paper 1  
        **Key concepts (Scheme of Work):** KC4

        ## Overview

        CPU architecture, machine-level thinking, and bit-level operations used in systems programming.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Processor Fundamen   |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Central Processing Uni… |
                     +-----------+
                            |
                     +-----v-----+
                     | Assembly Language     |
                     +-----------+
                            |
                     +-----v-----+
                     | Bit Manipulation      |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Von Neumann model; stored program; registers (general vs special: PC, MDR, MAR, ACC, IX, CIR, Status).
- ALU, CU, clock, IAS; buses (address, data, control); performance factors (cores, bus width, clock, cache).
- Ports (USB, HDMI, VGA); fetch–execute cycle with register transfer notation.
- Interrupts: causes, uses, ISR, timing within F–E cycle.
- Assembly vs machine code; two-pass assembler stages; trace simple programs.
- Instruction groups: data movement, I/O, arithmetic, unconditional/conditional, compare.
- Addressing modes: immediate, direct, indirect, indexed, relative; use syllabus instruction set.
- Logical, arithmetic, cyclic shifts (left/right).
- Bit masking to test/set bits; device monitor/control applications.
- AND, OR, XOR, LSL, LSR on ACC per syllabus.

        - **Scheme of Work:** suggested **15** guided hours; teaching order **3**.

        ## Key terms

        `Von Neumann`, `fetch-execute`, `register`, `interrupt`, `assembler`, `bit shift`, `masking`

        ## Real-world applications

        - Firmware
- Device drivers
- Performance tuning

        ## Subtopics (full modules)

        - **Central Processing Unit (CPU) Architecture** — [notes](subtopics/cpu-architecture/notes.md) · [examples](subtopics/cpu-architecture/examples.md) · [exercises](subtopics/cpu-architecture/exercises.md) · [solutions](subtopics/cpu-architecture/solutions.md) · [animation](subtopics/cpu-architecture/animation.md) · `animations/scene.py`
- **Assembly Language** — [notes](subtopics/assembly-language/notes.md) · [examples](subtopics/assembly-language/examples.md) · [exercises](subtopics/assembly-language/exercises.md) · [solutions](subtopics/assembly-language/solutions.md) · [animation](subtopics/assembly-language/animation.md) · `animations/scene.py`
- **Bit Manipulation** — [notes](subtopics/bit-manipulation/notes.md) · [examples](subtopics/bit-manipulation/examples.md) · [exercises](subtopics/bit-manipulation/exercises.md) · [solutions](subtopics/bit-manipulation/solutions.md) · [animation](subtopics/bit-manipulation/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
