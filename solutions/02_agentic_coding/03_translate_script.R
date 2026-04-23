# Solution 2.3: Translation of Python sequence utilities to R
# Using base R and stringr for string operations

library(stringr)

#' Calculate the GC content of a DNA sequence
#'
#' @param sequence A character string containing the DNA sequence (A, T, G, C).
#'   Both uppercase and lowercase are accepted.
#' @return A numeric value representing the GC content as a percentage (0–100).
#' @examples
#' calculate_gc_content("ATGCGC")  # returns 66.66667
#' calculate_gc_content("AAAA")    # returns 0
calculate_gc_content <- function(sequence) {
  sequence <- toupper(sequence)
  valid_bases <- c("A", "C", "G", "T")
  chars <- strsplit(sequence, "")[[1]]

  if (!all(chars %in% valid_bases)) {
    stop(paste("Invalid nucleotides in sequence:", sequence))
  }
  if (nchar(sequence) == 0) {
    return(0.0)
  }
  gc_count <- sum(chars %in% c("G", "C"))
  return((gc_count / nchar(sequence)) * 100.0)
}


#' Transcribe a DNA sequence to RNA
#'
#' Replaces all thymine (T/t) with uracil (U/u), preserving the original case.
#'
#' @param sequence A character string containing the DNA sequence.
#' @return A character string representing the RNA transcript.
#' @examples
#' transcribe_dna_to_rna("ATGCTT")  # returns "AUGCUU"
#' transcribe_dna_to_rna("atgctt")  # returns "augcuu"
transcribe_dna_to_rna <- function(sequence) {
  sequence_upper <- toupper(sequence)
  valid_bases <- c("A", "C", "G", "T")
  chars <- strsplit(sequence_upper, "")[[1]]

  if (!all(chars %in% valid_bases)) {
    stop(paste("Invalid nucleotides in sequence:", sequence))
  }
  rna <- chartr("Tt", "Uu", sequence)
  return(rna)
}


#' Return the reverse complement of a DNA sequence
#'
#' @param sequence A character string containing the DNA sequence.
#' @return A character string containing the reverse complement (uppercase).
#' @examples
#' reverse_complement("ATGC")          # returns "GCAT"
#' reverse_complement("AAAAACCCGGT")   # returns "ACCGGGTTTT"
reverse_complement <- function(sequence) {
  sequence_upper <- toupper(sequence)
  valid_bases <- c("A", "C", "G", "T")
  chars <- strsplit(sequence_upper, "")[[1]]

  if (!all(chars %in% valid_bases)) {
    stop(paste("Invalid nucleotides in sequence:", sequence))
  }
  complement_map <- c(A = "T", T = "A", G = "C", C = "G")
  complemented <- complement_map[chars]
  return(paste(rev(complemented), collapse = ""))
}


#' Calculate the melting temperature (Tm) of a DNA primer
#'
#' Uses the Wallace rule for short primers (<= 13 bp):
#' \deqn{T_m = 2 \cdot (A + T) + 4 \cdot (G + C)}
#' Uses a simplified nearest-neighbour approximation for longer primers.
#'
#' @param sequence A character string containing the primer sequence (DNA).
#' @return A numeric value representing the melting temperature in degrees Celsius.
#' @examples
#' calculate_melting_temperature("ATGCGC")  # short primer — uses Wallace rule
calculate_melting_temperature <- function(sequence) {
  sequence_upper <- toupper(sequence)
  chars <- strsplit(sequence_upper, "")[[1]]
  n <- length(chars)
  gc_count <- sum(chars %in% c("G", "C"))
  at_count <- sum(chars %in% c("A", "T"))

  if (n <= 13) {
    tm <- 2.0 * at_count + 4.0 * gc_count
  } else {
    gc_percent <- (gc_count / n) * 100.0
    sodium_concentration <- 0.05
    tm <- 81.5 + 16.6 * log10(sodium_concentration) + 0.41 * gc_percent - 675.0 / n
  }
  return(round(tm, 2))
}


#' Find restriction enzyme recognition sites in a DNA sequence
#'
#' @param sequence A character string containing the DNA sequence to search.
#' @param enzyme_sites A named character vector mapping enzyme names to their
#'   recognition sequences. Example:
#'   \code{c(EcoRI = "GAATTC", BamHI = "GGATCC")}
#' @return A data frame with columns \code{enzyme} and \code{position}
#'   (0-indexed), sorted by position.
#' @examples
#' sites <- find_restriction_sites(
#'   "ATGCGAATTCGGATCC",
#'   c(EcoRI = "GAATTC", BamHI = "GGATCC")
#' )
find_restriction_sites <- function(sequence, enzyme_sites) {
  sequence_upper <- toupper(sequence)
  results <- list()

  for (enzyme in names(enzyme_sites)) {
    site <- toupper(enzyme_sites[[enzyme]])
    # gregexpr returns 1-indexed positions; convert to 0-indexed
    matches <- gregexpr(site, sequence_upper, fixed = TRUE)[[1]]
    if (matches[1] != -1) {
      for (pos in matches) {
        results <- c(results, list(data.frame(enzyme = enzyme, position = pos - 1L)))
      }
    }
  }

  if (length(results) == 0) {
    return(data.frame(enzyme = character(0), position = integer(0)))
  }

  result_df <- do.call(rbind, results)
  result_df <- result_df[order(result_df$position), ]
  rownames(result_df) <- NULL
  return(result_df)
}


# --- Main ---
test_sequence <- "ATGCGAATTCGGATCCATGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG"

cat("=== Sequence Analysis ===\n")
cat("Sequence:", test_sequence, "\n")
cat(sprintf("GC content: %.1f%%\n", calculate_gc_content(test_sequence)))
cat("RNA transcript:", transcribe_dna_to_rna(test_sequence), "\n")
cat("Reverse complement:", reverse_complement(test_sequence), "\n")
cat(sprintf("Melting temperature: %.2f °C\n", calculate_melting_temperature(test_sequence)))

enzyme_sites <- c(EcoRI = "GAATTC", BamHI = "GGATCC", HindIII = "AAGCTT")
sites <- find_restriction_sites(test_sequence, enzyme_sites)
cat("\nRestriction sites found:\n")
for (i in seq_len(nrow(sites))) {
  cat(sprintf("  %s at position %d\n", sites$enzyme[i], sites$position[i]))
}
