def read_fastq(file_path):
    """
    Reads a FASTQ file and yields (header, sequence, quality).
    """
    sequences = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            header = lines[i].strip()
            seq = lines[i+1].strip()
            qual = lines[i+3].strip()
            sequences.append((header, seq, qual))
    return sequences

def calculate_average_quality(qual_string):
    """
    Converts a Phred+33 quality string into an average numerical score.
    """
    total = sum(ord(char) - 33 for char in qual_string)
    return total / len(qual_string) if qual_string else 0
