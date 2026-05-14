import sys

codon_table = {
    'AUG': 'M', 'CGC': 'R', 'AAC': 'N', 'UAG': '*'
}

def translate(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        protein += codon_table.get(codon, '?')
    return protein

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(translate(sys.argv[1]))