read_fastq <- function(file_path) {
  # Reads a FASTQ file and yields (header, sequence, quality).
  sequences <- list()
  
  lines <- readLines(file_path)
  
  if (length(lines) > 0) {
    for (i in seq(1, length(lines), by = 4)) {
      header <- trimws(lines[i])
      seq <- trimws(lines[i+1])
      qual <- trimws(lines[i+3])
      sequences[[length(sequences) + 1]] <- list(header = header, sequence = seq, quality = qual)
    }
  }
  
  return(sequences)
}

calculate_average_quality <- function(qual_string) {
  # Converts a Phred+33 quality string into an average numerical score.
  if (nchar(qual_string) == 0) return(0)
  
  chars <- strsplit(qual_string, "")[[1]]
  total <- sum(sapply(chars, function(c) as.integer(charToRaw(c)) - 33))
  return(total / length(chars))
}
