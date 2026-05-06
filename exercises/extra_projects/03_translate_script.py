"""
Exercise 2.3: Translating a Python Script to R and C++

This Python script implements a basic analysis pipeline for gene expression data.
Your task is to translate it to:
  1. R  (target file: solutions/02_agentic_coding/03_translate_script.R)
  2. C++ (target file: solutions/02_agentic_coding/03_translate_script.cpp)

Instructions:
  1. Read through the Python code below and understand what it does
  2. Open Copilot Chat (Ctrl+Alt+I) and describe the translation task
  3. Review the generated R/C++ code for correctness
  4. Make any necessary corrections

Useful prompts:
  - "Translate the following Python function to R, using idiomatic R style
     with tidyverse packages where appropriate: [paste function]"
  - "Translate the following Python function to C++17 with standard library
     only (no external dependencies): [paste function]"
  - "This Python code uses pandas DataFrames. What is the equivalent data
     structure in R and C++?"

Note: The C++ translation does not need to handle file I/O or DataFrames —
focus on translating the core numerical algorithms only.
"""

import math
from typing import List, Tuple


def calculate_gc_content(sequence: str) -> float:
    """Calculate the GC content of a DNA sequence as a percentage."""
    sequence = sequence.upper()
    valid_bases = set("ACGT")
    if not all(base in valid_bases for base in sequence):
        raise ValueError(f"Invalid nucleotides in sequence: {sequence}")
    if len(sequence) == 0:
        return 0.0
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100.0


def transcribe_dna_to_rna(sequence: str) -> str:
    """Convert a DNA sequence to its RNA equivalent."""
    mapping = str.maketrans("TtAaCcGg", "UuAaCcGg")
    sequence_upper = sequence.upper()
    valid_bases = set("ACGT")
    if not all(base in valid_bases for base in sequence_upper):
        raise ValueError(f"Invalid nucleotides in sequence: {sequence}")
    return sequence.translate(mapping)


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    sequence_upper = sequence.upper()
    valid_bases = set("ACGT")
    if not all(base in valid_bases for base in sequence_upper):
        raise ValueError(f"Invalid nucleotides in sequence: {sequence}")
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement[base] for base in reversed(sequence_upper))


def calculate_melting_temperature(sequence: str) -> float:
    """
    Calculate the melting temperature (Tm) of a DNA primer.

    Uses the Wallace rule for short primers (<= 13 bp):
        Tm = 2 * (A + T) + 4 * (G + C)

    Uses the nearest-neighbour approximation for longer primers:
        Tm = 81.5 + 16.6 * log10([Na+]) + 0.41 * %GC - 675 / len
    (with [Na+] = 0.05 M as default)
    """
    sequence_upper = sequence.upper()
    n = len(sequence_upper)
    gc_count = sequence_upper.count("G") + sequence_upper.count("C")
    at_count = sequence_upper.count("A") + sequence_upper.count("T")

    if n <= 13:
        tm = 2.0 * at_count + 4.0 * gc_count
    else:
        gc_percent = (gc_count / n) * 100.0
        sodium_concentration = 0.05
        tm = (
            81.5
            + 16.6 * math.log10(sodium_concentration)
            + 0.41 * gc_percent
            - 675.0 / n
        )
    return round(tm, 2)


def find_restriction_sites(sequence: str, enzyme_sites: dict) -> List[Tuple[str, int]]:
    """
    Find restriction enzyme cut sites in a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence to search.
    enzyme_sites : dict
        Dictionary mapping enzyme names to their recognition sequences.
        Example: {"EcoRI": "GAATTC", "BamHI": "GGATCC"}

    Returns
    -------
    list of tuples
        Each tuple is (enzyme_name, position) for each match found.
        Positions are 0-indexed.
    """
    results = []
    sequence_upper = sequence.upper()
    for enzyme, site in enzyme_sites.items():
        site_upper = site.upper()
        start = 0
        while True:
            pos = sequence_upper.find(site_upper, start)
            if pos == -1:
                break
            results.append((enzyme, pos))
            start = pos + 1
    return sorted(results, key=lambda x: x[1])


if __name__ == "__main__":
    test_sequence = "ATGCGAATTCGGATCCATGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG"

    print("=== Sequence Analysis ===")
    print(f"Sequence: {test_sequence}")
    print(f"GC content: {calculate_gc_content(test_sequence):.1f}%")
    print(f"RNA transcript: {transcribe_dna_to_rna(test_sequence)}")
    print(f"Reverse complement: {reverse_complement(test_sequence)}")
    print(f"Melting temperature: {calculate_melting_temperature(test_sequence):.2f} °C")

    enzyme_sites = {"EcoRI": "GAATTC", "BamHI": "GGATCC", "HindIII": "AAGCTT"}
    sites = find_restriction_sites(test_sequence, enzyme_sites)
    print("\nRestriction sites found:")
    for enzyme, pos in sites:
        print(f"  {enzyme} at position {pos}")
