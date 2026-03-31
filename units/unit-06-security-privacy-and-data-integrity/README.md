# Security, Privacy and Data Integrity

        **Level:** AS Level · **Primary assessment:** Paper 1  
        **Key concepts (Scheme of Work):** KC3, KC5

        ## Overview

        Protecting systems and data from threats, and keeping data accurate through validation and verification.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Security, Privacy    |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Data Security         |
                     +-----------+
                            |
                     +-----v-----+
                     | Data Integrity        |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Define security, privacy, integrity; need to protect data and systems.
- Security measures from standalone PC to networks (accounts, passwords, biometrics, firewall, AV, encryption).
- Threats: malware, hackers, phishing, pharming; mitigation methods; access rights.
- How validation and verification support integrity.
- Validation: range, format, length, presence, existence, limit, check digit.
- Verification on entry (visual, double entry) and transfer (parity byte/block, checksum).

        - **Scheme of Work:** suggested **8** guided hours; teaching order **6**.

        ## Key terms

        `encryption`, `firewall`, `malware`, `validation`, `checksum`, `parity`

        ## Real-world applications

        - Online banking
- Healthcare records
- E-government

        ## Subtopics (full modules)

        - **Data Security** — [notes](subtopics/6.1-data-security/notes.md) · [examples](subtopics/6.1-data-security/examples.md) · [exercises](subtopics/6.1-data-security/exercises.md) · [solutions](subtopics/6.1-data-security/solutions.md) · [animation](subtopics/6.1-data-security/animation.md) · `animations/scene.py`
- **Data Integrity** — [notes](subtopics/6.2-data-integrity/notes.md) · [examples](subtopics/6.2-data-integrity/examples.md) · [exercises](subtopics/6.2-data-integrity/exercises.md) · [solutions](subtopics/6.2-data-integrity/solutions.md) · [animation](subtopics/6.2-data-integrity/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
