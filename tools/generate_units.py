#!/usr/bin/env python3
"""Generate units/ tree: README.md per unit + subtopics/*/notes|examples|exercises.md."""
from __future__ import annotations

import os
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
UNITS_DIR = ROOT / "units"

# Learning objectives (aligned to official 9618 syllabus wording, shortened for clarity).
OBJECTIVES: dict[str, list[str]] = {
    "data-representation": [
        "Understand binary magnitudes and binary vs decimal prefixes (kibi/kilo, mebi/mega, gibi/giga, tebi/tera).",
        "Use binary, denary, hexadecimal, BCD; one’s and two’s complement; convert between bases/representations.",
        "Perform binary addition and subtraction; explain overflow for signed integers.",
        "Describe practical uses of BCD and hexadecimal.",
        "Explain character data in binary form; know ASCII, extended ASCII, Unicode (no memorised code tables).",
    ],
    "multimedia-graphics-and-sound": [
        "Bitmaps: pixels, header, image/screen resolution, colour depth; estimate file size; effects on quality/size.",
        "Vectors: drawing objects, properties, drawing list; choose bitmap vs vector with justification.",
        "Sound: sampling, sampling rate, resolution, analogue vs digital; impact on file size and accuracy.",
    ],
    "compression": [
        "Explain why compression is needed; give examples of use.",
        "Compare lossy vs lossless; justify a method for a situation.",
        "Describe how text, bitmap, vector, and sound may be compressed, including run-length encoding (RLE).",
    ],
    "networks-including-the-internet": [
        "Purpose/benefits of network devices; LAN vs WAN; client–server vs peer-to-peer (roles, pros/cons, justify).",
        "Thin vs thick client; bus, star, mesh, hybrid topologies; packet paths; justify topology.",
        "Cloud computing (public/private), benefits/drawbacks; wired vs wireless; media characteristics.",
        "LAN hardware: switch, server, NIC/WNIC, WAP, cables, bridge, repeater; router role.",
        "Ethernet, CSMA/CD; bit streaming (real-time vs on-demand) and bit rates.",
        "WWW vs internet; internet hardware (modem, PSTN, dedicated lines, cellular).",
        "IPv4/IPv6 format, subnetting, static vs dynamic, public vs private IPs; DNS and URLs.",
    ],
    "computers-and-their-components": [
        "Need for input, output, primary memory, secondary/removable storage; embedded systems pros/cons.",
        "Principal operations of listed devices (e.g. laser/3D printer, mic, speakers, HDD, SSD, optical, touchscreen, VR).",
        "Buffers; RAM vs ROM; SRAM vs DRAM; PROM, EPROM, EEPROM.",
        "Monitoring vs control; sensors and actuators; feedback.",
    ],
    "logic-gates-and-logic-circuits": [
        "Use symbols for NOT, AND, OR, NAND, NOR, XOR; two inputs except NOT.",
        "Truth tables for each gate; build circuit from statement, expression, or table (and reverse).",
    ],
    "cpu-architecture": [
        "Von Neumann model; stored program; registers (general vs special: PC, MDR, MAR, ACC, IX, CIR, Status).",
        "ALU, CU, clock, IAS; buses (address, data, control); performance factors (cores, bus width, clock, cache).",
        "Ports (USB, HDMI, VGA); fetch–execute cycle with register transfer notation.",
        "Interrupts: causes, uses, ISR, timing within F–E cycle.",
    ],
    "assembly-language": [
        "Assembly vs machine code; two-pass assembler stages; trace simple programs.",
        "Instruction groups: data movement, I/O, arithmetic, unconditional/conditional, compare.",
        "Addressing modes: immediate, direct, indirect, indexed, relative; use syllabus instruction set.",
    ],
    "bit-manipulation": [
        "Logical, arithmetic, cyclic shifts (left/right).",
        "Bit masking to test/set bits; device monitor/control applications.",
        "AND, OR, XOR, LSL, LSR on ACC per syllabus.",
    ],
    "operating-systems": [
        "Why an OS is needed; key tasks: memory, file, security, hardware/peripheral, process management.",
        "Utility software (formatter, antivirus, defrag, disk tools, compression, backup).",
        "Program libraries; benefits of library/DLL code in development.",
    ],
    "language-translators": [
        "Need for assembler, compiler, interpreter; benefits/drawbacks; justify choice.",
        "Awareness of hybrid compile/interpret (e.g. Java console mode).",
        "Typical IDE features: coding aids, syntax checks, pretty-print, debugging (step, breakpoints, watch).",
    ],
    "data-security": [
        "Define security, privacy, integrity; need to protect data and systems.",
        "Security measures from standalone PC to networks (accounts, passwords, biometrics, firewall, AV, encryption).",
        "Threats: malware, hackers, phishing, pharming; mitigation methods; access rights.",
    ],
    "data-integrity": [
        "How validation and verification support integrity.",
        "Validation: range, format, length, presence, existence, limit, check digit.",
        "Verification on entry (visual, double entry) and transfer (parity byte/block, checksum).",
    ],
    "ethics-and-ownership": [
        "Need/purpose of ethics for computing professionals; professional bodies (e.g. BCS, IEEE).",
        "Ethical vs unethical impact in scenarios; copyright; licence types and justification (FSF, OSI, shareware, commercial).",
        "AI: social, economic, environmental impact; applications of AI.",
    ],
    "database-concepts": [
        "Limitations of file-based storage/retrieval vs relational model features.",
        "Relational terminology: entity, table, record, field, tuple, attribute, keys, relationships, referential integrity, indexing.",
        "E–R diagrams; normalisation to 1NF, 2NF, 3NF; explain/produce normalised designs.",
    ],
    "database-management-systems": [
        "DBMS features vs file-based approach: dictionary, modelling, logical schema, integrity, security, backup, access rights.",
        "Developer interface; query processor roles.",
    ],
    "ddl-and-dml": [
        "DDL vs DML; SQL as industry standard; read/write simple DDL/DML as per syllabus subset.",
        "CREATE DATABASE/TABLE with listed data types; ALTER; PRIMARY KEY; FOREIGN KEY.",
        "Queries on ≤2 tables: SELECT, WHERE, ORDER BY, GROUP BY, INNER JOIN, aggregates; INSERT/DELETE/UPDATE.",
    ],
    "computational-thinking-skills": [
        "Abstraction: purpose, benefits, modelling essentials only.",
        "Decomposition into sub-problems and modules (procedures/functions).",
    ],
    "algorithms": [
        "Algorithms as defined steps; identifier tables; pseudocode with input–process–output.",
        "Sequence, selection, iteration; document with structured English, flowchart, or pseudocode.",
        "Translate between structured English, flowchart, and pseudocode; stepwise refinement; logic statements.",
    ],
    "data-types-and-records": [
        "Choose INTEGER, REAL, CHAR, STRING, BOOLEAN, DATE, ARRAY, FILE as appropriate.",
        "Purpose of records; pseudocode to define/read/write records.",
    ],
    "arrays": [
        "Terms: index, bounds; choose 1D/2D; pseudocode declarations and processing.",
        "Bubble sort; linear search.",
    ],
    "files": [
        "Why files exist; pseudocode for text files with one or more lines.",
    ],
    "introduction-to-abstract-data-types": [
        "ADT = data + operations; stack, queue, linked list — features and justification.",
        "Manipulate data in these structures (no pseudocode for structure ops at AS intro).",
        "Implement stack, queue, linked list using arrays.",
    ],
    "programming-basics": [
        "Implement pseudocode from flowchart/structured English.",
        "Declarations, assignment, expressions, console I/O; built-in/library routines as provided in exam.",
    ],
    "constructs": [
        "IF/ELSE (nested), CASE; count-controlled, post-condition, pre-condition loops; justify loop choice.",
    ],
    "structured-programming": [
        "Procedures and functions; parameters by value/reference; headers, interfaces, arguments, return values.",
        "When to use procedures vs functions; write efficient pseudocode.",
    ],
    "program-development-lifecycle": [
        "Purpose of life cycles; waterfall, iterative, RAD — principles, pros/cons.",
        "Analysis, design, coding, testing, maintenance stages.",
    ],
    "program-design": [
        "Structure charts: decomposition, parameters between modules; purpose; derive pseudocode.",
        "State-transition diagrams: purpose in documenting algorithms.",
    ],
    "program-testing-and-maintenance": [
        "Syntax, logic, runtime errors; locate and correct.",
        "Testing methods: dry run, walkthrough, white/black box, integration, alpha, beta, acceptance, stubs.",
        "Test strategy/plan; normal, abnormal, boundary data.",
        "Maintenance types: perfective, adaptive, corrective; enhance given programs.",
    ],
    "user-defined-data-types": [
        "Why user-defined types are needed; enumerated, pointer; set, record, class/object; design for problem.",
    ],
    "file-organisation-and-access": [
        "Serial, sequential (key), random (record key); appropriate organisation/access.",
        "Sequential vs direct access; hashing to read/write random/sequential files.",
    ],
    "floating-point-representation": [
        "Binary floating-point format; two’s complement; mantissa/exponent trade-offs; denary conversion.",
        "Normalisation; approximation, rounding error; underflow/overflow.",
    ],
    "protocols": [
        "Why protocols matter; layered stacks and responsibilities.",
        "TCP/IP four layers; message path between hosts.",
        "HTTP, FTP, POP3, IMAP, SMTP, BitTorrent purposes.",
    ],
    "circuit-switching-and-packet-switching": [
        "Circuit switching: benefits, drawbacks, where used.",
        "Packet switching: benefits, drawbacks; router role; message delivery across networks/internet.",
    ],
    "processors-parallel-processing-and-virtual-machines": [
        "RISC vs CISC; interrupts on both; pipelining/registers in RISC.",
        "Flynn: SISD, SIMD, MISD, MIMD; massively parallel systems.",
        "Virtual machines: concept, examples, benefits, limitations.",
    ],
    "boolean-algebra-and-logic-circuits": [
        "Truth tables including half/full adders; multi-input gates possible.",
        "SR/JK flip-flops: circuit, table, storage role.",
        "Boolean algebra, De Morgan’s laws, simplification; Karnaugh maps: benefits and use.",
    ],
    "purposes-of-an-operating-system": [
        "OS maximising resource use; UI hiding hardware complexity.",
        "Processes: multitasking, states (running, ready, blocked), scheduling algorithms.",
        "Kernel, interrupts, low-level scheduling; virtual memory, paging, segmentation, page replacement, thrashing.",
    ],
    "translation-software": [
        "Interpreter execution without full translated program; compiler stages: lexical/syntax analysis, code gen, optimisation.",
        "Syntax diagrams or BNF; Reverse Polish Notation evaluation.",
    ],
    "encryption-and-digital-certificates": [
        "Symmetric vs asymmetric; keys, plaintext/ciphertext; private messaging and verified public messages.",
        "Quantum cryptography awareness; SSL/TLS purpose and use cases.",
        "Digital certificates and digital signatures.",
    ],
    "artificial-intelligence": [
        "Graphs for AI: structure; A* and Dijkstra (interpret given algorithms, not write graph setup).",
        "Neural networks and machine learning; deep, reinforcement learning; supervised vs unsupervised.",
        "Back propagation and regression (conceptual).",
    ],
    "algorithms-and-adts": [
        "Linear vs binary search — write, conditions for binary, performance vs size.",
        "Insertion sort and bubble sort — write; performance depends on order and n.",
        "ADT operations: search/insert/delete on linked list, binary tree; stack, queue, linked list algorithms.",
        "Graph as ADT; implementing ADTs from built-ins or other ADTs; dictionary, binary tree.",
        "Compare algorithms; Big O for time and space.",
    ],
    "recursion": [
        "Essential features; expression in a HLL; write and trace recursive algorithms.",
        "When recursion helps; compiler work (stacks, unwinding) — awareness.",
    ],
    "programming-paradigms": [
        "Meaning of paradigm; characteristics of low-level, imperative/procedural, OOP, declarative.",
        "Low-level: addressing modes; procedural: variables, constructs, subprograms; OOP: classes, inheritance, polymorphism, encapsulation, etc.; declarative: facts, rules, goals.",
    ],
    "file-processing-and-exception-handling": [
        "Open/close files (read, write, append); read/write records; serial, sequential, random processing.",
        "Exceptions: importance, when to handle; write exception handling code.",
    ],
}

UNITS: list[dict] = [
    {
        "folder": "unit-01-information-representation",
        "title": "Information Representation",
        "level": "AS Level",
        "paper": "Paper 1 (sections 1–8)",
        "sow_hours": 12,
        "sow_order": 1,
        "kc": ["KC5"],
        "overview": "How numbers, text, images, sound, and compressed data are stored as bits, and how choices affect size and quality.",
        "key_terms": ["binary", "hexadecimal", "BCD", "two's complement", "Unicode", "sampling", "lossy", "lossless", "RLE"],
        "applications": ["Streaming media", "Medical imaging", "Game assets", "Mobile bandwidth"],
        "subtopics": [
            ("data-representation", "Data Representation"),
            ("multimedia-graphics-and-sound", "Multimedia — Graphics and Sound"),
            ("compression", "Compression"),
        ],
    },
    {
        "folder": "unit-02-communication",
        "title": "Communication",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 16,
        "sow_order": 4,
        "kc": ["KC3"],
        "overview": "How devices share data from LANs to the global internet, including models, hardware, and addressing.",
        "key_terms": ["LAN", "WAN", "TCP/IP", "DNS", "URL", "topology", "router", "cloud"],
        "applications": ["Remote learning", "E-commerce", "Video conferencing", "IoT"],
        "subtopics": [("networks-including-the-internet", "Networks Including the Internet")],
    },
    {
        "folder": "unit-03-hardware",
        "title": "Hardware",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 11,
        "sow_order": 2,
        "kc": ["KC4"],
        "overview": "Physical components from embedded systems to peripherals, memory technologies, and combinational logic.",
        "key_terms": ["RAM", "ROM", "SRAM", "DRAM", "sensor", "actuator", "logic gate", "truth table"],
        "applications": ["Factory automation", "Wearables", "Autonomous vehicles"],
        "subtopics": [
            ("computers-and-their-components", "Computers and Their Components"),
            ("logic-gates-and-logic-circuits", "Logic Gates and Logic Circuits"),
        ],
    },
    {
        "folder": "unit-04-processor-fundamentals",
        "title": "Processor Fundamentals",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 15,
        "sow_order": 3,
        "kc": ["KC4"],
        "overview": "CPU architecture, machine-level thinking, and bit-level operations used in systems programming.",
        "key_terms": ["Von Neumann", "fetch-execute", "register", "interrupt", "assembler", "bit shift", "masking"],
        "applications": ["Firmware", "Device drivers", "Performance tuning"],
        "subtopics": [
            ("cpu-architecture", "Central Processing Unit (CPU) Architecture"),
            ("assembly-language", "Assembly Language"),
            ("bit-manipulation", "Bit Manipulation"),
        ],
    },
    {
        "folder": "unit-05-system-software",
        "title": "System Software",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 8,
        "sow_order": 7,
        "kc": ["KC4"],
        "overview": "Operating systems and translators that make hardware usable and turn source code into running programs.",
        "key_terms": ["OS", "compiler", "interpreter", "IDE", "library", "DLL"],
        "applications": ["Multi-user servers", "Software development", "System utilities"],
        "subtopics": [
            ("operating-systems", "Operating Systems"),
            ("language-translators", "Language Translators"),
        ],
    },
    {
        "folder": "unit-06-security-privacy-and-data-integrity",
        "title": "Security, Privacy and Data Integrity",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 8,
        "sow_order": 6,
        "kc": ["KC3", "KC5"],
        "overview": "Protecting systems and data from threats, and keeping data accurate through validation and verification.",
        "key_terms": ["encryption", "firewall", "malware", "validation", "checksum", "parity"],
        "applications": ["Online banking", "Healthcare records", "E-government"],
        "subtopics": [
            ("data-security", "Data Security"),
            ("data-integrity", "Data Integrity"),
        ],
    },
    {
        "folder": "unit-07-ethics-and-ownership",
        "title": "Ethics and Ownership",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 6,
        "sow_order": 5,
        "kc": ["KC1"],
        "overview": "Professional responsibility, intellectual property, licensing, and the societal impact of computing and AI.",
        "key_terms": ["copyright", "open source", "shareware", "professional ethics", "AI impact"],
        "applications": ["Software licences", "Data consent", "Responsible AI deployment"],
        "subtopics": [("ethics-and-ownership", "Ethics and Ownership")],
    },
    {
        "folder": "unit-08-databases",
        "title": "Databases",
        "level": "AS Level",
        "paper": "Paper 1",
        "sow_hours": 18,
        "sow_order": 9,
        "kc": ["KC5"],
        "overview": "Relational design, normalisation, DBMS features, and practical SQL for defining and querying data.",
        "key_terms": ["primary key", "foreign key", "normalisation", "SQL", "DDL", "DML", "ER diagram"],
        "applications": ["Airline booking", "Library systems", "Inventory"],
        "subtopics": [
            ("database-concepts", "Database Concepts"),
            ("database-management-systems", "Database Management Systems (DBMS)"),
            ("ddl-and-dml", "DDL and DML (SQL)"),
        ],
    },
    {
        "folder": "unit-09-algorithm-design-and-problem-solving",
        "title": "Algorithm Design and Problem-solving",
        "level": "AS Level",
        "paper": "Paper 2",
        "sow_hours": 28,
        "sow_order": 0,
        "kc": ["KC1"],
        "overview": "Computational thinking skills and clear algorithm design using pseudocode, flowcharts, and refinement.",
        "key_terms": ["abstraction", "decomposition", "pseudocode", "flowchart", "stepwise refinement"],
        "applications": ["Automation", "Business processes", "Scientific computing"],
        "subtopics": [
            ("computational-thinking-skills", "Computational Thinking Skills"),
            ("algorithms", "Algorithms"),
        ],
    },
    {
        "folder": "unit-10-data-types-and-structures",
        "title": "Data Types and Structures",
        "level": "AS Level",
        "paper": "Paper 2",
        "sow_hours": 22,
        "sow_order": 0,
        "kc": ["KC1", "KC5"],
        "overview": "Choosing data types, using records and arrays, simple file handling, and introductory ADTs.",
        "key_terms": ["record", "array", "index", "stack", "queue", "linked list", "ADT"],
        "applications": ["Queues in scheduling", "Grids in games", "Text processing"],
        "subtopics": [
            ("data-types-and-records", "Data Types and Records"),
            ("arrays", "Arrays"),
            ("files", "Files"),
            ("introduction-to-abstract-data-types", "Introduction to Abstract Data Types (ADT)"),
        ],
    },
    {
        "folder": "unit-11-programming",
        "title": "Programming",
        "level": "AS Level",
        "paper": "Paper 2",
        "sow_hours": 24,
        "sow_order": 0,
        "kc": ["KC1", "KC2"],
        "overview": "Writing structured pseudocode with correct constructs, modular design, and clear interfaces.",
        "key_terms": ["variable", "constant", "procedure", "function", "parameter", "loop", "selection"],
        "applications": ["Console utilities", "Data processing", "Embedded logic"],
        "subtopics": [
            ("programming-basics", "Programming Basics"),
            ("constructs", "Constructs"),
            ("structured-programming", "Structured Programming"),
        ],
    },
    {
        "folder": "unit-12-software-development",
        "title": "Software Development",
        "level": "AS Level",
        "paper": "Paper 2",
        "sow_hours": 12,
        "sow_order": 8,
        "kc": ["KC1"],
        "overview": "Life cycles, design notations, disciplined testing, and maintaining reliable software.",
        "key_terms": ["waterfall", "RAD", "structure chart", "black-box testing", "maintenance"],
        "applications": ["Start-up MVPs", "Safety-critical updates", "User acceptance"],
        "subtopics": [
            ("program-development-lifecycle", "Program Development Life Cycle"),
            ("program-design", "Program Design"),
            ("program-testing-and-maintenance", "Program Testing and Maintenance"),
        ],
    },
    {
        "folder": "unit-13-data-representation-a-level",
        "title": "Data Representation (A Level)",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 15,
        "sow_order": 10,
        "kc": ["KC5"],
        "overview": "Richer types, file organisation with hashing, and floating-point representation including errors.",
        "key_terms": ["enumerated type", "pointer", "hashing", "mantissa", "exponent", "normalisation"],
        "applications": ["Scientific computing", "Large-scale indexes", "Financial systems"],
        "subtopics": [
            ("user-defined-data-types", "User-defined Data Types"),
            ("file-organisation-and-access", "File Organisation and Access"),
            ("floating-point-representation", "Floating-point Representation and Manipulation"),
        ],
    },
    {
        "folder": "unit-14-communication-and-internet-technologies",
        "title": "Communication and Internet Technologies",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 15,
        "sow_order": 13,
        "kc": ["KC3"],
        "overview": "Protocol stacks, internet applications, and how switching strategies shape networks.",
        "key_terms": ["TCP/IP", "HTTP", "FTP", "packet switching", "circuit switching", "router"],
        "applications": ["CDN", "Email", "P2P distribution"],
        "subtopics": [
            ("protocols", "Protocols"),
            ("circuit-switching-and-packet-switching", "Circuit Switching and Packet Switching"),
        ],
    },
    {
        "folder": "unit-15-hardware-and-virtual-machines",
        "title": "Hardware and Virtual Machines",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 15,
        "sow_order": 11,
        "kc": ["KC4"],
        "overview": "Advanced processors, parallelism, virtualisation, and formal logic tools for digital design.",
        "key_terms": ["RISC", "CISC", "MIMD", "virtual machine", "Karnaugh map", "flip-flop"],
        "applications": ["Cloud data centres", "GPU computing", "CPU design"],
        "subtopics": [
            ("processors-parallel-processing-and-virtual-machines", "Processors, Parallel Processing and Virtual Machines"),
            ("boolean-algebra-and-logic-circuits", "Boolean Algebra and Logic Circuits"),
        ],
    },
    {
        "folder": "unit-16-system-software-a-level",
        "title": "System Software (A Level)",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 15,
        "sow_order": 12,
        "kc": ["KC4"],
        "overview": "Deepening OS ideas (scheduling, memory) and how translators analyse and evaluate code.",
        "key_terms": ["scheduler", "paging", "thrashing", "lexical analysis", "BNF", "RPN"],
        "applications": ["Server OS tuning", "Language implementation", "Compilers"],
        "subtopics": [
            ("purposes-of-an-operating-system", "Purposes of an Operating System"),
            ("translation-software", "Translation Software"),
        ],
    },
    {
        "folder": "unit-17-security-a-level",
        "title": "Security (A Level)",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 10,
        "sow_order": 14,
        "kc": ["KC3"],
        "overview": "Modern cryptography, secure channels, and trust through certificates and signatures.",
        "key_terms": ["public key", "symmetric", "TLS", "digital certificate", "digital signature"],
        "applications": ["HTTPS e-commerce", "Email signing", "VPN concepts"],
        "subtopics": [("encryption-and-digital-certificates", "Encryption, Protocols and Digital Certificates")],
    },
    {
        "folder": "unit-18-artificial-intelligence",
        "title": "Artificial Intelligence (AI)",
        "level": "A Level",
        "paper": "Paper 3",
        "sow_hours": 10,
        "sow_order": 15,
        "kc": ["KC1"],
        "overview": "Search on graphs, core machine learning ideas, and how neural methods support intelligent behaviour.",
        "key_terms": ["A*", "Dijkstra", "supervised learning", "neural network", "back propagation"],
        "applications": ["Navigation", "Recommendation", "Computer vision"],
        "subtopics": [("artificial-intelligence", "Artificial Intelligence")],
    },
    {
        "folder": "unit-19-computational-thinking-and-problem-solving",
        "title": "Computational Thinking and Problem-solving",
        "level": "A Level",
        "paper": "Papers 3–4",
        "sow_hours": 50,
        "sow_order": 0,
        "kc": ["KC1", "KC5"],
        "overview": "Advanced algorithms, ADT operations, complexity, and recursion for Paper 3 and practical work.",
        "key_terms": ["binary search", "Big O", "recursion", "binary tree", "ADT implementation"],
        "applications": ["Search engines", "Compilers", "Simulation"],
        "subtopics": [
            ("algorithms-and-adts", "Algorithms and Abstract Data Types"),
            ("recursion", "Recursion"),
        ],
    },
    {
        "folder": "unit-20-further-programming",
        "title": "Further Programming",
        "level": "A Level",
        "paper": "Papers 3–4",
        "sow_hours": 50,
        "sow_order": 0,
        "kc": ["KC2"],
        "overview": "Multiple paradigms and production-style file handling with exceptions for robust programs.",
        "key_terms": ["OOP", "declarative", "inheritance", "exception", "random file"],
        "applications": ["Enterprise apps", "Plugins", "Data pipelines"],
        "subtopics": [
            ("programming-paradigms", "Programming Paradigms"),
            ("file-processing-and-exception-handling", "File Processing and Exception Handling"),
        ],
    },
]


def write_notes(unit_title: str, sub_title: str, slug: str) -> str:
    objs = OBJECTIVES.get(slug, ["Follow the official syllabus for this subtopic."])
    obj_bullets = "\n".join(f"- {o}" for o in objs)
    return dedent(
        f"""\
        # {sub_title}

        ## Definition and explanation

        This subtopic is part of **{unit_title}** in Cambridge International AS & A Level Computer Science **9618**. It builds practical understanding you can apply in exams and real systems: focus on **definitions**, **when to use each idea**, and **short written justifications** as well as calculations or algorithms where relevant.

        ## Syllabus learning objectives

        {obj_bullets}

        ## Diagrams

        ```
        +------------------+      +------------------+
        |   Placeholder    | ---> | Add a diagram    |
        |   (your sketch)  |      | or Mermaid here  |
        +------------------+      +------------------+
        ```

        _Contributors: replace this box with an ASCII diagram, Mermaid, or an image in `resources/diagrams/`._

        ## Key concepts

        {obj_bullets}

        ## Important exam points

        - Use **Cambridge command words** precisely (*state*, *describe*, *explain*, *justify*).
        - Link **technical terms** to the scenario given in the question.
        - Show **working** for numeric or trace questions.

        💡 **Exam Tip:** For “justify” questions, give **two balanced points** (e.g. benefit + limitation) tied to the context.

        ⚠️ **Common Mistakes:** Writing vague answers without **syllabus terminology**; confusing similar terms (e.g. validation vs verification; lossy vs lossless).

        🔗 **Further Reading:** [Cambridge 9618 syllabus](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-computer-science-9618/) · School Support Hub (registered centres)
        """
    ).strip() + "\n"


def write_examples(unit_title: str, sub_title: str, slug: str) -> str:
    return dedent(
        f"""\
        # Worked examples — {sub_title}

        ## Example 1 — Concept check (short)

        **Prompt:** Give one reason why the syllabus expects you to connect **theory** to a **short scenario**.

        **Worked answer:** The syllabus tests **application (AO2)**. A good answer names a **concept**, applies it to the **scenario**, and uses **because** to link evidence.

        ---

        ## Example 2 — Structured steps

        **Prompt:** Outline how you would approach a multi-part algorithm question under time pressure.

        **Steps:**

        1. Read all parts; underline **outputs** and **constraints**.
        2. Write an **identifier table** if variables are non-trivial.
        3. Code **pseudocode** with clear **indentation** and **END** markers for structures.
        4. Dry-run **one** normal case if a trace is requested.

        **Code snippet (pseudocode style):**

        ```
        // Illustrative only — match the official pseudocode guide in exams
        CONSTANT MaxN = 100
        DECLARE Count : INTEGER
        Count ← 0
        WHILE Count < MaxN DO
          OUTPUT Count
          Count ← Count + 1
        ENDWHILE
        ```

        💡 **Exam Tip:** If the insert provides **built-in functions**, prefer those names exactly.

        ⚠️ **Common Mistakes:** Mixing **language-specific** syntax with **exam pseudocode**; forgetting **ENDWHILE** / **ENDIF**.

        🔗 **Further Reading:** Pseudocode guide PDF in `resources/references/originals/`
        """
    ).strip() + "\n"


def write_exercises(unit_title: str, sub_title: str, slug: str) -> str:
    return dedent(
        f"""\
        # Exercises — {sub_title}

        _Original exam-style questions only. Do not copy Cambridge past papers verbatim._

        ## Short answer

        1. **Define** one key term from `{sub_title}` using syllabus-quality wording.
        2. **State** one real-world application and **link** it to a technical idea from this subtopic.
        3. **Give** one advantage and one limitation of a method discussed in `{sub_title}`.

        ## Structured question

        A school is updating its systems. A scenario will describe users, devices, and data.

        1. **Describe** how a concept from **{unit_title}** applies to the scenario.  
        2. **Explain** why an alternative approach might be weaker **in this context**.  
        3. **Justify** a recommendation that balances **performance**, **security**, and **usability** (choose factors relevant to `{sub_title}`).

        ## Scenario-based

        You are advising a small organisation that must keep records consistent and secure.

        - **Identify** two **risks** relevant to `{sub_title}`.  
        - **Outline** controls or design choices that address those risks.  
        - **Evaluate** trade-offs (e.g. cost, complexity, user friction).

        💡 **Exam Tip:** Use **headings** in longer answers to mirror the question parts.

        ⚠️ **Common Mistakes:** Answering a **different** topic than the question stem; **lists** without **explanations** where the command word is *explain* or *justify*.

        🔗 **Further Reading:** Specimen papers on the School Support Hub (registered centres)
        """
    ).strip() + "\n"


def unit_readme(u: dict) -> str:
    sub_links = "\n".join(
        f"- [{t}](subtopics/{s}/notes.md) · [examples](subtopics/{s}/examples.md) · [exercises](subtopics/{s}/exercises.md)"
        for s, t in u["subtopics"]
    )
    sow = u["sow_order"]
    sow_line = (
        f"- **Scheme of Work:** suggested **{u['sow_hours']}** guided hours; teaching order **{sow}**."
        if sow
        else f"- **Scheme of Work:** **{u['sow_hours']}** guided hours; integrate **continuously** across the course."
    )
    kc = ", ".join(u["kc"])
    terms = ", ".join(f"`{t}`" for t in u["key_terms"])
    apps = "\n".join(f"- {a}" for a in u["applications"])
    objectives = []
    for slug, _st in u["subtopics"]:
        for line in OBJECTIVES.get(slug, []):
            objectives.append(f"- {line}")
    obj_block = "\n".join(objectives)

    return dedent(
        f"""\
        # {u["title"]}

        **Level:** {u["level"]} · **Primary assessment:** {u["paper"]}  
        **Key concepts (Scheme of Work):** {kc}

        ## Overview

        {u["overview"]}

        ## Learning objectives

        Derived from the official **9618** syllabus and cross-checked with the **Scheme of Work** (topic sequencing and key concept tags):

        {obj_block}

        {sow_line}

        ## Key terms

        {terms}

        ## Real-world applications

        {apps}

        ## Subtopics

        {sub_links}
        """
    ).strip() + "\n"


def main() -> None:
    UNITS_DIR.mkdir(parents=True, exist_ok=True)
    for u in UNITS:
        udir = UNITS_DIR / u["folder"]
        udir.mkdir(parents=True, exist_ok=True)
        (udir / "README.md").write_text(unit_readme(u), encoding="utf-8")
        for slug, stitle in u["subtopics"]:
            sdir = udir / "subtopics" / slug
            sdir.mkdir(parents=True, exist_ok=True)
            (sdir / "notes.md").write_text(write_notes(u["title"], stitle, slug), encoding="utf-8")
            (sdir / "examples.md").write_text(write_examples(u["title"], stitle, slug), encoding="utf-8")
            (sdir / "exercises.md").write_text(write_exercises(u["title"], stitle, slug), encoding="utf-8")
    print(f"Generated {len(UNITS)} units under {UNITS_DIR}")


if __name__ == "__main__":
    main()
