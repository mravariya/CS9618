# System Software (A Level)

        **Level:** A Level · **Primary assessment:** Paper 3  
        **Key concepts (Scheme of Work):** KC4

        ## Overview

        Deepening OS ideas (scheduling, memory) and how translators analyse and evaluate code.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   System Software (A   |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Purposes of an Operati… |
                     +-----------+
                            |
                     +-----v-----+
                     | Translation Software  |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - OS maximising resource use; UI hiding hardware complexity.
- Processes: multitasking, states (running, ready, blocked), scheduling algorithms.
- Kernel, interrupts, low-level scheduling; virtual memory, paging, segmentation, page replacement, thrashing.
- Interpreter execution without full translated program; compiler stages: lexical/syntax analysis, code gen, optimisation.
- Syntax diagrams or BNF; Reverse Polish Notation evaluation.

        - **Scheme of Work:** suggested **15** guided hours; teaching order **12**.

        ## Key terms

        `scheduler`, `paging`, `thrashing`, `lexical analysis`, `BNF`, `RPN`

        ## Real-world applications

        - Server OS tuning
- Language implementation
- Compilers

        ## Subtopics (full modules)

        - **Purposes of an Operating System** — [notes](subtopics/purposes-of-an-operating-system/notes.md) · [examples](subtopics/purposes-of-an-operating-system/examples.md) · [exercises](subtopics/purposes-of-an-operating-system/exercises.md) · [solutions](subtopics/purposes-of-an-operating-system/solutions.md) · [animation](subtopics/purposes-of-an-operating-system/animation.md) · `animations/scene.py`
- **Translation Software** — [notes](subtopics/translation-software/notes.md) · [examples](subtopics/translation-software/examples.md) · [exercises](subtopics/translation-software/exercises.md) · [solutions](subtopics/translation-software/solutions.md) · [animation](subtopics/translation-software/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
