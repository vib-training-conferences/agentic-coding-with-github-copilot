call_variants <- function(reference, alignments) {
  # Identifies variants by comparing aligned reads to the reference.
  # 
  # Args:
  #   reference (character): The reference DNA sequence.
  #   alignments (list): List of lists containing 'read_sequence' and 'starting_position'.
  # 
  # Returns:
  #   list: A list mapping positions to found variants (ref_base, alt_base).
  
  variants <- list()
  
  for (align in alignments) {
    read_seq <- align$read_sequence
    pos <- align$starting_position
    
    if (pos == -1) {
      next
    }
    
    bases <- strsplit(read_seq, "")[[1]]
    ref_bases <- strsplit(reference, "")[[1]]
    
    for (i in seq_along(bases)) {
      base <- bases[i]
      ref_pos <- pos + (i - 1) + 1
      if (ref_pos <= length(ref_bases)) {
        ref_base <- ref_bases[ref_pos]
        if (base != ref_base) {
          pos_str <- as.character(ref_pos)
          if (is.null(variants[[pos_str]])) {
            variants[[pos_str]] <- list()
          }
          variants[[pos_str]] <- append(variants[[pos_str]], list(list(ref = ref_base, alt = base)))
        }
      }
    }
  }
  
  return(variants)
}
