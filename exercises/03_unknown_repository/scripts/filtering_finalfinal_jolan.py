def filter_high_quality_variants(variants, min_depth=5):
    """
    Filters variant calls based on minimum read depth.
    There is a bug in this function where it modifies a dictionary while iterating over it.
    """
    for position in variants.keys():
        observations = variants[position]
        if len(observations) < min_depth:
            del variants[position]
            
    return variants

def write_vcf(filtered_variants, output_file):
    with open(output_file, 'w') as f:
        f.write("##fileformat=VCFv4.2\n")
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
        
        for pos, obs in filtered_variants.items():
            ref = obs[0]['ref']
            alt = obs[0]['alt']
            depth = len(obs)
            f.write(f"chr1\t{pos}\t.\t{ref}\t{alt}\t.\tPASS\tDP={depth}\n")
