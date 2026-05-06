# Exercise 2.1: Writing Functions with GitHub Copilot Autocomplete

## Learning Objective

Explore the different ways GitHub Copilot can help you write functions in VS Code — from inline autocomplete to agent-generated code. You will also observe the **stochastic nature** of LLM-generated code by running the same prompt multiple times and comparing the outputs.

---

## Background

GitHub Copilot offers several modes for generating code:
1. **Autocomplete** — Copilot completes code as you type (triggered automatically or with `Tab`)
2. **Inline chat** — Ask Copilot to generate or modify code in-context (`Ctrl+I`)
3. **Copilot Chat sidebar** — Full conversation interface for complex tasks
4. **Agent mode** — Give Copilot a high-level task and let it plan and execute across multiple files

> **Key insight**: LLMs are stochastic — the same prompt can produce different outputs each time. This is both a strength (you can explore multiple implementations) and a weakness (you cannot rely on reproducibility). Always review the output.

---

## Part 1: Autocomplete from a Comment

### Instructions

1. Create a new file `sequence_utils.py`
2. Type the following comment and press `Enter`. Wait for Copilot to suggest a function:

```python
# Calculate the melting temperature of a DNA primer using the Wallace rule
```

3. Press `Tab` to accept the suggestion, or `Alt+]` / `Alt+[` to cycle through alternative suggestions
4. Try accepting and then asking for the next suggestion — are they different?

**Wallace rule** (for primers ≤ 13 bp):  
`Tm = 2°C × (A + T) + 4°C × (G + C)`

Check whether Copilot's implementation uses the correct formula.

---

## Part 2: Autocomplete from a Function Definition and Docstring

### Instructions

Type the following function definition **including the docstring**, then stop and let Copilot complete the function body:

```python
def parse_fasta(filepath: str) -> dict:
    """
    Parse a FASTA file and return a dictionary of sequences.

    Parameters
    ----------
    filepath : str
        Path to the FASTA file.

    Returns
    -------
    dict
        Dictionary where keys are sequence identifiers (without the '>' prefix)
        and values are the corresponding nucleotide sequences as strings.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file is not in valid FASTA format.
    """
```

Press `Tab` to accept Copilot's completion. Evaluate the generated code:
- Does it correctly handle multi-line sequences?
- Does it raise the specified exceptions?
- Is the code readable?

---

## Part 3: Prompting Copilot via Inline Chat

### Instructions

1. Place your cursor in `sequence_utils.py` (below your existing functions)
2. Press `Ctrl+I` to open **inline chat**
3. Type the following prompt:

```
Write a function called `find_orfs` that finds all open reading frames in a DNA sequence. An ORF starts with ATG and ends with TAA, TAG, or TGA. Return a list of tuples (start, end, sequence) for each ORF found in the forward strand only.
```

4. Review the generated code carefully:
   - Does it handle overlapping ORFs?
   - Does it correctly identify the stop codons?
   - Does it handle sequences that are not multiples of 3?

---

## Part 4: Observe the Stochastic Nature of LLMs

### Instructions

This part demonstrates that Copilot (and all LLMs) are non-deterministic.

1. **Delete the `find_orfs` function** you just generated
2. Press `Ctrl+I` again and use the **exact same prompt** as in Part 3
3. Compare the new output to the previous one

**Questions:**
- Are the two implementations identical?
- Do they both produce correct results?
- Are there any differences in style, variable names, or algorithm?

Repeat this 2–3 more times. You should observe variations in the output.

> This is important for **reproducibility**: if you use Copilot to generate code for a scientific workflow, document the final code carefully — you cannot reproduce Copilot's exact output later.

---

## Part 5: Using More Context to Guide the Output

### Instructions

The quality of Copilot's output depends heavily on the **context** available to it — the code already in the file, comments, imports, and the structure of existing functions.

1. Add the following import and constant to the top of your file:

```python
from typing import Optional

CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}
```

2. Now ask Copilot (inline chat or autocomplete) to write a function:

```
# Translate a DNA sequence to protein using CODON_TABLE
def translate_dna(sequence: str, reading_frame: int = 0) -> str:
```

Does Copilot now use the `CODON_TABLE` you defined? Compare this to what it would generate without the table being in context.

---

## Reflection

1. **Which approach was most effective** for getting high-quality code: comment-based autocomplete, docstring-guided completion, or inline chat?
2. **What happened when you reprompted** with the same prompt? How different were the outputs?
3. **How did adding the CODON_TABLE** change Copilot's output? What does this tell you about the importance of context?
4. **Critical review**: Go through each function Copilot generated and identify at least one potential issue or improvement.

---

## Bonus: Measure Output Variability

Run the same prompt 5 times and record:
- Variable names used
- Algorithm approach (e.g., iterative vs list comprehension)
- Edge case handling
- Approximate length of the function

This exercise illustrates that LLMs are tools that require careful human oversight — they are assistants, not authorities.
