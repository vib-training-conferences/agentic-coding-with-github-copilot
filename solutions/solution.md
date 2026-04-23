
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

1. **Validation logic inverted** — `>= 0` should be `< 0` to catch negative values
2. **Division by zero / log(0)** — missing pseudocount in `compute_log2_fold_change`
3. **One-tailed p-value** — `stats.norm.sf` should use `stats.t.sf` × 2 for two-tailed
4. **Wrong data source in `add_pvalues`** — used `result_df` instead of `original_df`
5. **Bonferroni correction not capped** — adjusted p-values must be clipped to 1.0
6. **Absolute value missing** — `get_significant_genes` should filter on `abs(log2_fc)`
7. **Welch's t-test not used** — standard t-distribution used without checking variance equality
