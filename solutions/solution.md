
# Solutions for Agentic Coding with GitHub Copilot

## Session 01: Chat-Based Coding

Solutions for chat-based exercises are intentionally open-ended — the exact output
depends on the prompts used and the LLM's stochastic responses. The exercise
markdown files contain expected outputs and verification steps to check correctness.

## Session 02: Agentic Coding

| Exercise | Solution File | Notes |
|----------|--------------|-------|
| 2.2 Add documentation | `02_agentic_coding/02_add_documentation.py` | NumPy-style docstrings for all functions |
| 2.3 Translate to R | `02_agentic_coding/03_translate_script.R` | Idiomatic R with base R |
| 2.3 Translate to C++ | `02_agentic_coding/03_translate_script.cpp` | C++17, standard library only |
| 2.4 Debugging (fixed) | `02_agentic_coding/04_debugging_fixed.py` | All 7 bugs fixed with explanations |

### Bug list for Exercise 2.4

| # | Function | Bug description | Fix |
|---|----------|----------------|-----|
| 1 | `load_and_validate_data` | Validation condition is inverted (`>= 0` raises for valid data) | Change to `< 0` |
| 2 | `compute_log2_fold_change` | No pseudocount — causes division by zero and `log2(0) = -inf` | Add `pseudocount=1.0` to both means |
| 3 | `compute_simple_pvalue` | Wrong standard error formula: `sqrt(var1 + var2)` ignores sample sizes | Use `sqrt(var1/n1 + var2/n2)` |
| 4 | `compute_simple_pvalue` | One-tailed p-value using normal distribution for n=3 samples | Use two-tailed t-test with Welch's degrees of freedom |
| 5 | `add_pvalues` | Expression values looked up from `result_df` (no raw columns) | Look up from `original_df` |
| 6 | `apply_multiple_testing_correction` | Adjusted p-values not capped at 1.0 | Add `.clip(upper=1.0)` |
| 7 | `get_significant_genes` | Missing `abs()` — only upregulated genes pass the threshold | Filter on `abs(log2_fold_change)` |
