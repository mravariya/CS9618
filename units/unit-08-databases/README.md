# Databases

        **Level:** AS Level · **Primary assessment:** Paper 1  
        **Key concepts (Scheme of Work):** KC5

        ## Overview

        Relational design, normalisation, DBMS features, and practical SQL for defining and querying data.

        ## Concept map (text)

        ```text
                            +----------------------+
                    |   Databases            |
                    +----------+-----------+
                            |
                     +-----v-----+
                     | Database Concepts     |
                     +-----------+
                            |
                     +-----v-----+
                     | Database Management Sy… |
                     +-----------+
                            |
                     +-----v-----+
                     | DDL and DML (SQL)     |
                     +-----------+
        ```

        ## Learning objectives (syllabus-mapped)

        - Limitations of file-based storage/retrieval vs relational model features.
- Relational terminology: entity, table, record, field, tuple, attribute, keys, relationships, referential integrity, indexing.
- E–R diagrams; normalisation to 1NF, 2NF, 3NF; explain/produce normalised designs.
- DBMS features vs file-based approach: dictionary, modelling, logical schema, integrity, security, backup, access rights.
- Developer interface; query processor roles.
- DDL vs DML; SQL as industry standard; read/write simple DDL/DML as per syllabus subset.
- CREATE DATABASE/TABLE with listed data types; ALTER; PRIMARY KEY; FOREIGN KEY.
- Queries on ≤2 tables: SELECT, WHERE, ORDER BY, GROUP BY, INNER JOIN, aggregates; INSERT/DELETE/UPDATE.

        - **Scheme of Work:** suggested **18** guided hours; teaching order **9**.

        ## Key terms

        `primary key`, `foreign key`, `normalisation`, `SQL`, `DDL`, `DML`, `ER diagram`

        ## Real-world applications

        - Airline booking
- Library systems
- Inventory

        ## Subtopics (full modules)

        - **Database Concepts** — [notes](subtopics/8.1-database-concepts/notes.md) · [examples](subtopics/8.1-database-concepts/examples.md) · [exercises](subtopics/8.1-database-concepts/exercises.md) · [solutions](subtopics/8.1-database-concepts/solutions.md) · [animation](subtopics/8.1-database-concepts/animation.md) · `animations/scene.py`
- **Database Management Systems (DBMS)** — [notes](subtopics/8.2-database-management-systems/notes.md) · [examples](subtopics/8.2-database-management-systems/examples.md) · [exercises](subtopics/8.2-database-management-systems/exercises.md) · [solutions](subtopics/8.2-database-management-systems/solutions.md) · [animation](subtopics/8.2-database-management-systems/animation.md) · `animations/scene.py`
- **DDL and DML (SQL)** — [notes](subtopics/8.3-ddl-and-dml/notes.md) · [examples](subtopics/8.3-ddl-and-dml/examples.md) · [exercises](subtopics/8.3-ddl-and-dml/exercises.md) · [solutions](subtopics/8.3-ddl-and-dml/solutions.md) · [animation](subtopics/8.3-ddl-and-dml/animation.md) · `animations/scene.py`

        ## Animations (Manim)

        From any subtopic folder, install dependencies (see root `README.md`), then:

        `manim -pql animations/scene.py <SceneName>`
