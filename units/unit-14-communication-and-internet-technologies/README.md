# Communication and Internet Technologies

        **Level:** A Level · **Primary assessment:** Paper 3  
        **Key concepts (Scheme of Work):** KC3

        ## Overview

        Protocol stacks, internet applications, and how switching strategies shape networks.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Communication and    |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Protocols             |
                     +-----------+
                            |
                     +-----v-----+
                     | Circuit Switching and … |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Why protocols matter; layered stacks and responsibilities.
- TCP/IP four layers; message path between hosts.
- HTTP, FTP, POP3, IMAP, SMTP, BitTorrent purposes.
- Circuit switching: benefits, drawbacks, where used.
- Packet switching: benefits, drawbacks; router role; message delivery across networks/internet.

        - **Scheme of Work:** suggested **15** guided hours; teaching order **13**.

        ## Key terms

        `TCP/IP`, `HTTP`, `FTP`, `packet switching`, `circuit switching`, `router`

        ## Real-world applications

        - CDN
- Email
- P2P distribution

        ## Subtopics (full modules)

        - **Protocols** — [notes](subtopics/14.1-protocols/notes.md) · [examples](subtopics/14.1-protocols/examples.md) · [exercises](subtopics/14.1-protocols/exercises.md) · [solutions](subtopics/14.1-protocols/solutions.md) · [animation](subtopics/14.1-protocols/animation.md) · `animations/scene.py`
- **Circuit Switching and Packet Switching** — [notes](subtopics/14.2-circuit-switching-and-packet-switching/notes.md) · [examples](subtopics/14.2-circuit-switching-and-packet-switching/examples.md) · [exercises](subtopics/14.2-circuit-switching-and-packet-switching/exercises.md) · [solutions](subtopics/14.2-circuit-switching-and-packet-switching/solutions.md) · [animation](subtopics/14.2-circuit-switching-and-packet-switching/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
