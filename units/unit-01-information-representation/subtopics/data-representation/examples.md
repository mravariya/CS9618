# Worked examples — Data Representation

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
