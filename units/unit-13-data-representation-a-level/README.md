# Data Representation (A Level)

        **Level:** A Level · **Primary assessment:** Paper 3  
        **Key concepts (Scheme of Work):** KC5

        ## Overview

        Richer types, file organisation with hashing, and floating-point representation including errors.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Data Representatio   |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | User-defined Data Type… |
                     +-----------+
                            |
                     +-----v-----+
                     | File Organisation and … |
                     +-----------+
                            |
                     +-----v-----+
                     | Floating-point Represe… |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Why user-defined types are needed; enumerated, pointer; set, record, class/object; design for problem.
- Serial, sequential (key), random (record key); appropriate organisation/access.
- Sequential vs direct access; hashing to read/write random/sequential files.
- Binary floating-point format; two’s complement; mantissa/exponent trade-offs; denary conversion.
- Normalisation; approximation, rounding error; underflow/overflow.

        - **Scheme of Work:** suggested **15** guided hours; teaching order **10**.

        ## Key terms

        `enumerated type`, `pointer`, `hashing`, `mantissa`, `exponent`, `normalisation`

        ## Real-world applications

        - Scientific computing
- Large-scale indexes
- Financial systems

        ## Subtopics (full modules)

        - **User-defined Data Types** — [notes](subtopics/13.1-user-defined-data-types/notes.md) · [examples](subtopics/13.1-user-defined-data-types/examples.md) · [exercises](subtopics/13.1-user-defined-data-types/exercises.md) · [solutions](subtopics/13.1-user-defined-data-types/solutions.md) · [animation](subtopics/13.1-user-defined-data-types/animation.md) · `animations/scene.py`
- **File Organisation and Access** — [notes](subtopics/13.2-file-organisation-and-access/notes.md) · [examples](subtopics/13.2-file-organisation-and-access/examples.md) · [exercises](subtopics/13.2-file-organisation-and-access/exercises.md) · [solutions](subtopics/13.2-file-organisation-and-access/solutions.md) · [animation](subtopics/13.2-file-organisation-and-access/animation.md) · `animations/scene.py`
- **Floating-point Representation and Manipulation** — [notes](subtopics/13.3-floating-point-representation/notes.md) · [examples](subtopics/13.3-floating-point-representation/examples.md) · [exercises](subtopics/13.3-floating-point-representation/exercises.md) · [solutions](subtopics/13.3-floating-point-representation/solutions.md) · [animation](subtopics/13.3-floating-point-representation/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
