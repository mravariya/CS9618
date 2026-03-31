# Information Representation

        **Level:** AS Level · **Primary assessment:** Paper 1 (sections 1–8)  
        **Key concepts (Scheme of Work):** KC5

        ## Overview

        How numbers, text, images, sound, and compressed data are stored as bits, and how choices affect size and quality.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Information Repres   |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Data Representation   |
                     +-----------+
                            |
                     +-----v-----+
                     | Multimedia — Graphics … |
                     +-----------+
                            |
                     +-----v-----+
                     | Compression           |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Understand binary magnitudes and binary vs decimal prefixes (kibi/kilo, mebi/mega, gibi/giga, tebi/tera).
- Use binary, denary, hexadecimal, BCD; one’s and two’s complement; convert between bases/representations.
- Perform binary addition and subtraction; explain overflow for signed integers.
- Describe practical uses of BCD and hexadecimal.
- Explain character data in binary form; know ASCII, extended ASCII, Unicode (no memorised code tables).
- Bitmaps: pixels, header, image/screen resolution, colour depth; estimate file size; effects on quality/size.
- Vectors: drawing objects, properties, drawing list; choose bitmap vs vector with justification.
- Sound: sampling, sampling rate, resolution, analogue vs digital; impact on file size and accuracy.
- Explain why compression is needed; give examples of use.
- Compare lossy vs lossless; justify a method for a situation.
- Describe how text, bitmap, vector, and sound may be compressed, including run-length encoding (RLE).

        - **Scheme of Work:** suggested **12** guided hours; teaching order **1**.

        ## Key terms

        `binary`, `hexadecimal`, `BCD`, `two's complement`, `Unicode`, `sampling`, `lossy`, `lossless`, `RLE`

        ## Real-world applications

        - Streaming media
- Medical imaging
- Game assets
- Mobile bandwidth

        ## Subtopics (full modules)

        - **Data Representation** — [notes](subtopics/data-representation/notes.md) · [examples](subtopics/data-representation/examples.md) · [exercises](subtopics/data-representation/exercises.md) · [solutions](subtopics/data-representation/solutions.md) · [animation](subtopics/data-representation/animation.md) · `animations/scene.py`
- **Multimedia — Graphics and Sound** — [notes](subtopics/multimedia-graphics-and-sound/notes.md) · [examples](subtopics/multimedia-graphics-and-sound/examples.md) · [exercises](subtopics/multimedia-graphics-and-sound/exercises.md) · [solutions](subtopics/multimedia-graphics-and-sound/solutions.md) · [animation](subtopics/multimedia-graphics-and-sound/animation.md) · `animations/scene.py`
- **Compression** — [notes](subtopics/compression/notes.md) · [examples](subtopics/compression/examples.md) · [exercises](subtopics/compression/exercises.md) · [solutions](subtopics/compression/solutions.md) · [animation](subtopics/compression/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
