# Solutions — Data Representation (1.1)

## A. Short answer

1. **1 GiB** = 2^30 bytes (= 1 073 741 824 bytes).
2. **1 GB** (SI, decimal) = 10^9 bytes (= 1 000 000 000 bytes) when used in that sense.
3. **Two’s complement:** fixed-width signed encoding where negatives are formed by **inverting bits and adding 1** (modulo 2^n), so subtraction can reuse addition hardware.

## B. Structured

1. **91** = 64 + 16 + 8 + 2 + 1 → **`01011011`**.
2. Unsigned: 64 + 8 + 4 + 2 = **78**.
3. Nibbles `0100` `1110` → **4E** (hex).
4. **−96:** +96 = `01100000`; invert → `10011111`; +1 → **`10100000`** (8-bit two’s complement).

## C. Exam-style (model reasoning)

1. **Explain overflow:** If the true sum ≥ 2^(n−1) for the positive range, the bit pattern becomes the **sign bit = 1**, i.e. looks **negative** in two’s complement → inconsistent with “two positives” expectation → overflow.
2. **BCD situation:** when **exact decimal digit** fidelity matters (e.g. currency step of 0.01 in some embedded/legacy designs) or **direct drive** of decimal displays—accept answers referencing rounding in binary integer/float.
3. **Justify hex:** fewer symbols than binary → fewer transcription errors; maps cleanly to **nibbles** and **byte-aligned** memory views.

## D. Scenario

- **Interpretations:** 10^6 bytes per “MB” vs 2^20 bytes per “MiB” (or ambiguous “MB”).
- **Documentation:** prevents user mistrust, support tickets, and data loss when users estimate downloads/backups.

---

Cross-check methods with your teacher against the **current** 9618 syllabus for your series.
