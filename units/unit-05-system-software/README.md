# System Software

        **Level:** AS Level · **Primary assessment:** Paper 1  
        **Key concepts (Scheme of Work):** KC4

        ## Overview

        Operating systems and translators that make hardware usable and turn source code into running programs.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   System Software      |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Operating Systems     |
                     +-----------+
                            |
                     +-----v-----+
                     | Language Translators  |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Why an OS is needed; key tasks: memory, file, security, hardware/peripheral, process management.
- Utility software (formatter, antivirus, defrag, disk tools, compression, backup).
- Program libraries; benefits of library/DLL code in development.
- Need for assembler, compiler, interpreter; benefits/drawbacks; justify choice.
- Awareness of hybrid compile/interpret (e.g. Java console mode).
- Typical IDE features: coding aids, syntax checks, pretty-print, debugging (step, breakpoints, watch).

        - **Scheme of Work:** suggested **8** guided hours; teaching order **7**.

        ## Key terms

        `OS`, `compiler`, `interpreter`, `IDE`, `library`, `DLL`

        ## Real-world applications

        - Multi-user servers
- Software development
- System utilities

        ## Subtopics (full modules)

        - **Operating Systems** — [notes](subtopics/5.1-operating-systems/notes.md) · [examples](subtopics/5.1-operating-systems/examples.md) · [exercises](subtopics/5.1-operating-systems/exercises.md) · [solutions](subtopics/5.1-operating-systems/solutions.md) · [animation](subtopics/5.1-operating-systems/animation.md) · `animations/scene.py`
- **Language Translators** — [notes](subtopics/5.2-language-translators/notes.md) · [examples](subtopics/5.2-language-translators/examples.md) · [exercises](subtopics/5.2-language-translators/exercises.md) · [solutions](subtopics/5.2-language-translators/solutions.md) · [animation](subtopics/5.2-language-translators/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
