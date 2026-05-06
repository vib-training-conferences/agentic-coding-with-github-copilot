build_kmer_index <- function(reference, k=15) {
  index <- list()
  ref_len <- nchar(reference)
  
  if (ref_len >= k) {
    for (i in 1:(ref_len - k + 1)) {
      kmer <- substr(reference, i, i + k - 1)
      pos_1based <- i
      if (is.null(index[[kmer]])) {
        index[[kmer]] <- c()
      }
      index[[kmer]] <- c(index[[kmer]], pos_1based)
    }
  }
  
  return(index)
}

align_read <- function(read_seq, reference, kmer_index, k=15) {
  read_kmer <- substr(read_seq, 1, k)
  
  if (!is.null(kmer_index[[read_kmer]])) {
    for (pos in kmer_index[[read_kmer]]) {
      ref_sub <- substr(reference, pos, pos + nchar(read_seq) - 1)
      if (ref_sub == read_seq) {
        return(pos)
      }
    }
  }
  
  return(-1)
}
