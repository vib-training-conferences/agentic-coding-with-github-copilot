def call_variants(reference, alignments):
    """
    Identifies variants by comparing aligned reads to the reference.
    
    Args:
        reference (str): The reference DNA sequence.
        alignments (list): List of tuples containing (read_sequence, starting_position).
        
    Returns:
        dict: A dictionary mapping positions to found variants (ref_base, alt_base).
    """
    variants = {}
    for read_seq, pos in alignments:
        if pos == -1:
            continue
            
        for i, base in enumerate(read_seq):
            ref_pos = pos + i
            if ref_pos < len(reference):
                ref_base = reference[ref_pos]
                if base != ref_base:
                    if ref_pos not in variants:
                        variants[ref_pos] = []
                    variants[ref_pos].append({'ref': ref_base, 'alt': base})
                    
    return variants
