import sys

def analyze(protein):
    hydrophobic = ['M', 'A', 'V', 'L', 'I', 'P', 'F', 'W']
    count = 0
    for aa in protein:
        if aa in hydrophobic:
            count += 1
    
    # Intentional bug: concatenating string and int
    print("Total amino acids: " + len(protein))
    print("Hydrophobic count: " + count)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze(sys.argv[1])