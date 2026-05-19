filter_high_quality_variants <- function(variants, min_depth = 5) {
  # Filters variant calls based on minimum read depth.
  for (i in 1:length(variants)) {
    observations <- variants[[i]]
    if (length(observations) < min_depth) {
      variants[[i]] <- NULL
    }
  }
  return(variants)
}

write_vcf <- function(filtered_variants, output_file) {
  con <- file(output_file, "w")
  writeLines("##fileformat=VCFv4.2", con)
  writeLines("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO", con)
  
  for (pos in names(filtered_variants)) {
    obs <- filtered_variants[[pos]]
    ref <- obs[[1]]$ref
    alt <- obs[[1]]$alt
    depth <- length(obs)
    writeLines(sprintf("chr1\t%s\t.\t%s\t%s\t.\tPASS\tDP=%d", pos, ref, alt, depth), con)
  }
  close(con)
}
