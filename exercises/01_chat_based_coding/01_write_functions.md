# Exercise 1.1: Writing Functions with GitHub Copilot Chat

## Learning Objective

Learn how to use GitHub Copilot Chat to write new Python functions from a natural-language description. You will discover that Copilot can generate functional code quickly, but you must always **review and test** the output.

---

## Background

GitHub Copilot Chat allows you to describe a coding task in plain language and receive a code suggestion in return. This is useful for:
- Quickly prototyping functions
- Generating boilerplate code
- Exploring how to implement an algorithm

> **Key insight**: Copilot generates *plausible* code based on patterns in its training data. It can make mistakes — especially in edge cases or domain-specific logic. Always verify the output.

---

## Exercise

Open a new Python file (`exercise_01.py`) in VS Code. Use **Copilot Chat** (click the chat icon in the sidebar or press `Ctrl+Alt+I`) to ask Copilot to write the following functions. After each function, test it manually to check whether the output is correct.

### Task 1: GC Content Calculator

Ask Copilot to write a function that calculates the **GC content** of a DNA sequence.

**Suggested prompt:**
```
Write a Python function called `calculate_gc_content` that takes a DNA sequence string as input and returns the percentage of G and C nucleotides. The function should handle both uppercase and lowercase input and raise a ValueError if the sequence contains invalid characters.
```

**Expected behavior:**
- `calculate_gc_content("ATGCGC")` → `66.67`
- `calculate_gc_content("AAAA")` → `0.0`
- `calculate_gc_content("GCGC")` → `100.0`
- `calculate_gc_content("ATXG")` → raises `ValueError`

**Questions to consider:**
1. Does Copilot's implementation handle empty strings? What should happen?
2. Does it handle the case where only `G` or only `C` nucleotides are present?
3. How does it handle lowercase input?

---

### Task 2: DNA to RNA Transcription

Ask Copilot to write a function that **transcribes a DNA sequence to RNA**.

**Suggested prompt:**
```
Write a Python function called `transcribe_dna_to_rna` that converts a DNA sequence to its RNA equivalent by replacing all thymine (T) with uracil (U). The function should preserve case and raise a ValueError for invalid nucleotides.
```

**Expected behavior:**
- `transcribe_dna_to_rna("ATGCTT")` → `"AUGCUU"`
- `transcribe_dna_to_rna("atgctt")` → `"augcuu"`

---

### Task 3: Reverse Complement

Ask Copilot to write a function that returns the **reverse complement** of a DNA sequence.

**Suggested prompt:**
```
Write a Python function called `reverse_complement` that takes a DNA sequence and returns its reverse complement. Use the standard Watson-Crick base pairing rules (A↔T, G↔C). Handle both uppercase and lowercase input.
```

**Expected behavior:**
- `reverse_complement("ATGC")` → `"GCAT"`
- `reverse_complement("AAAAACCCGGT")` → `"ACCGGGTTTT"`

---

## Reflection

After completing the tasks:

1. **Did Copilot generate correct code on the first try?** If not, what was wrong?
2. **How did you verify the output?** Writing tests is a good practice — did Copilot offer to help with that too?
3. **Try reprompting**: If the first output was not quite right, try rephrasing your prompt. How does the output change?
4. **Limits of Copilot Chat**: Ask Copilot to write a function that translates a DNA codon to an amino acid using the full genetic code table. How confident are you in the accuracy of the output?

---

## Tips

- You can ask Copilot Chat to **explain** a piece of code: select it, right-click → "Copilot > Explain"
- You can ask Copilot to **add error handling**, **add tests**, or **improve performance** after it generates the initial code
- Use the **thumbs up/down** feedback buttons in the chat to help improve Copilot
