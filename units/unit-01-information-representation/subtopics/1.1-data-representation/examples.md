# Guided examples — Data Representation (1.1)

---

## Example 1 — Denary to binary (unsigned, 8-bit)

**Task:** Convert denary **205** to an 8-bit binary pattern.

**Working (division by 2, remainders least significant first):**

205 ÷ 2 = 102 r **1**  
102 ÷ 2 = 51 r **0**  
51 ÷ 2 = 25 r **1**  
25 ÷ 2 = 12 r **1**  
12 ÷ 2 = 6 r **0**  
6 ÷ 2 = 3 r **0**  
3 ÷ 2 = 1 r **1**  
1 ÷ 2 = 0 r **1**

Read remainders from bottom to top: **11001101**

**Check:** 128 + 64 + 8 + 4 + 1 = 205. ✓

---

## Example 2 — Binary to hexadecimal

**Task:** `11001101` → hex.

**Working:** Split into nibbles from the right: `1100` `1101`  
`1100` = 12 → **C**  
`1101` = 13 → **D**  
Result: **0xCD** (exam style may write **CD₁₆** or `&CD` in assembly contexts).

---

## Example 3 — Two’s complement, 8-bit: represent −42

**Method:** Positive 42 in 8 bits is `00101010`. Invert → `11010101`. Add 1 → `11010110`.

**Check idea:** Add `00101010` + `11010110` = `1 00000000` → discard carry out → `00000000`.

---

## Example 4 — Prefix comparison (KiB vs KB)

**Statement:** “Download speed 100 MB/s” vs “file size 100 MiB.”

**Explain:** **MB** often uses decimal 10^6 in networking/marketing; **MiB** is 2^20 bytes by IEC definition. Close in wording, different magnitudes—precision matters in exams when comparing storage vs transfer claims.

---

## Example 5 — BCD vs pure binary for denary 39

- **Unsigned 8-bit binary:** `00100111` (one byte, value 39)
- **BCD (two digits):** `0011` `1001` (nibble 3, nibble 9)

**Justify BCD:** easier mapping to **seven-segment** / decimal business rules; **cost:** less compact than binary integer encoding.

💡 **Exam Tip:** When asked to **justify**, always give **criteria** (accuracy, hardware, human factors, storage).

🔗 **Further Reading:** Official syllabus PDF in `resources/references/originals/`
