def build_kmer_index(reference, k=15):
    index = {}
    for i in range(len(reference) - k + 1):
        kmer = reference[i:i+k]
        if kmer not in index:
            index[kmer] = []
        index[kmer].append(i)
    return index

def align_read(read_seq, reference, kmer_index, k=15):
    read_kmer = read_seq[:k]
    if read_kmer in kmer_index:
        for pos in kmer_index[read_kmer]:
            if reference[pos:pos+len(read_seq)] == read_seq:
                return pos
    return -1
