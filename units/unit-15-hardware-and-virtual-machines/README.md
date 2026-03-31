# Hardware and Virtual Machines

        **Level:** A Level · **Primary assessment:** Paper 3  
        **Key concepts (Scheme of Work):** KC4

        ## Overview

        Advanced processors, parallelism, virtualisation, and formal logic tools for digital design.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Hardware and Virtu   |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Processors, Parallel P… |
                     +-----------+
                            |
                     +-----v-----+
                     | Boolean Algebra and Lo… |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - RISC vs CISC; interrupts on both; pipelining/registers in RISC.
- Flynn: SISD, SIMD, MISD, MIMD; massively parallel systems.
- Virtual machines: concept, examples, benefits, limitations.
- Truth tables including half/full adders; multi-input gates possible.
- SR/JK flip-flops: circuit, table, storage role.
- Boolean algebra, De Morgan’s laws, simplification; Karnaugh maps: benefits and use.

        - **Scheme of Work:** suggested **15** guided hours; teaching order **11**.

        ## Key terms

        `RISC`, `CISC`, `MIMD`, `virtual machine`, `Karnaugh map`, `flip-flop`

        ## Real-world applications

        - Cloud data centres
- GPU computing
- CPU design

        ## Subtopics (full modules)

        - **Processors, Parallel Processing and Virtual Machines** — [notes](subtopics/15.1-processors-parallel-processing-and-virtual-machines/notes.md) · [examples](subtopics/15.1-processors-parallel-processing-and-virtual-machines/examples.md) · [exercises](subtopics/15.1-processors-parallel-processing-and-virtual-machines/exercises.md) · [solutions](subtopics/15.1-processors-parallel-processing-and-virtual-machines/solutions.md) · [animation](subtopics/15.1-processors-parallel-processing-and-virtual-machines/animation.md) · `animations/scene.py`
- **Boolean Algebra and Logic Circuits** — [notes](subtopics/15.2-boolean-algebra-and-logic-circuits/notes.md) · [examples](subtopics/15.2-boolean-algebra-and-logic-circuits/examples.md) · [exercises](subtopics/15.2-boolean-algebra-and-logic-circuits/exercises.md) · [solutions](subtopics/15.2-boolean-algebra-and-logic-circuits/solutions.md) · [animation](subtopics/15.2-boolean-algebra-and-logic-circuits/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
