"""
Exercise 2.4: Debugging Faulty Scripts

This Python script is supposed to process gene expression data and identify
differentially expressed genes, but it contains SEVEN bugs.

Your tasks:
  1. Read the code and try to identify the bugs yourself first
  2. Run the script and observe the errors or unexpected output
  3. Use GitHub Copilot to help identify and fix the bugs
  4. Verify that the fixed script produces correct results

Hint: The bugs are a mix of:
  - Syntax/runtime errors (the script will crash)
  - Logic errors (the script runs but gives wrong results)
  - Edge case errors (the script fails on certain inputs)

Use these Copilot prompts to help debug:
  - "I get this error when running my script: [paste error]. Here is the
     relevant code: [paste code]. What is wrong?"
  - "This function is supposed to [description] but it returns [wrong value]
     instead of [expected value]. What is the bug?"
  - "Review this function for correctness: [paste function]"
"""

import numpy as np
import pandas as pd
from pathlib import Path


def load_and_validate_data(filepath):
    """Load gene expression data and validate required columns."""
    required_columns = [
        "gene_id", "gene_name",
        "ctrl_1", "ctrl_2", "ctrl_3",
        "treat_1", "treat_2", "treat_3"
    ]

    df = pd.read_csv(filepath)

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Bug 1: This check is inverted — it should raise if values ARE negative
    if (df[["ctrl_1", "ctrl_2", "ctrl_3", "treat_1", "treat_2", "treat_3"]] >= 0).all().all():
        raise ValueError("Expression values must be non-negative")

    return df


def compute_log2_fold_change(df):
    """Compute log2 fold change for each gene."""
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]

    mean_ctrl = df[control_cols].mean(axis=1)
    mean_treat = df[treatment_cols].mean(axis=1)

    # Bug 2: Division by zero is not handled; also log2 of 0 is -inf
    log2_fc = np.log2(mean_treat / mean_ctrl)

    result = df[["gene_id", "gene_name"]].copy()
    result["mean_ctrl"] = mean_ctrl
    result["mean_treat"] = mean_treat
    result["log2_fold_change"] = log2_fc
    return result


def compute_simple_pvalue(ctrl_values, treat_values):
    """
    Compute a simple two-sample t-test p-value.
    Returns the p-value (float between 0 and 1).
    """
    n1 = len(ctrl_values)
    n2 = len(treat_values)

    mean1 = np.mean(ctrl_values)
    mean2 = np.mean(treat_values)

    var1 = np.var(ctrl_values, ddof=1)
    var2 = np.var(treat_values, ddof=1)

    # Bug 3: Missing parentheses around (var1/n1 + var2/n2) causes wrong result
    se = np.sqrt(var1 / n1 + var2 / n2)

    if se == 0:
        return 1.0

    t_stat = (mean2 - mean1) / se

    # Approximate p-value using normal distribution (valid for large n, but here n=3)
    # Bug 4: This gives the one-tailed p-value; should be two-tailed (multiply by 2)
    from scipy import stats
    p_value = stats.norm.sf(abs(t_stat))
    return p_value


def add_pvalues(result_df, original_df):
    """Add p-values for each gene to the results DataFrame."""
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]

    pvalues = []
    for idx in result_df.index:
        gene_id = result_df.loc[idx, "gene_id"]

        # Bug 5: This uses result_df instead of original_df to get expression values
        gene_row = result_df[result_df["gene_id"] == gene_id].iloc[0]

        ctrl_vals = [gene_row.get(col, np.nan) for col in control_cols]
        treat_vals = [gene_row.get(col, np.nan) for col in treatment_cols]

        pval = compute_simple_pvalue(ctrl_vals, treat_vals)
        pvalues.append(pval)

    result_df = result_df.copy()
    result_df["p_value"] = pvalues
    return result_df


def apply_multiple_testing_correction(result_df, method="bonferroni"):
    """Apply multiple testing correction to p-values."""
    n_tests = len(result_df)

    if method == "bonferroni":
        # Bug 6: Bonferroni correction multiplies p-values (not divides the threshold)
        # but the multiplication should be capped at 1.0
        result_df = result_df.copy()
        result_df["p_value_adjusted"] = result_df["p_value"] * n_tests
        # Missing: cap adjusted p-values at 1.0
    else:
        raise ValueError(f"Unknown correction method: {method}")

    return result_df


def get_significant_genes(result_df, alpha=0.05, log2fc_threshold=1.0):
    """Return genes that are statistically significant and differentially expressed."""
    significant = result_df[
        (result_df["p_value_adjusted"] < alpha) &
        # Bug 7: Should use absolute value of log2_fold_change
        (result_df["log2_fold_change"] > log2fc_threshold)
    ].copy()

    return significant.sort_values("log2_fold_change", ascending=False)


if __name__ == "__main__":
    data_path = Path(__file__).parent.parent.parent / "data" / "gene_expression.csv"

    print("Loading data...")
    df = load_and_validate_data(data_path)
    print(f"  Loaded {len(df)} genes")

    print("Computing fold changes...")
    results = compute_log2_fold_change(df)

    print("Computing p-values...")
    results = add_pvalues(results, df)

    print("Applying multiple testing correction...")
    results = apply_multiple_testing_correction(results)

    print("Filtering significant genes...")
    significant = get_significant_genes(results)

    print(f"\nFound {len(significant)} significant differentially expressed genes:")
    print(significant[["gene_name", "log2_fold_change", "p_value", "p_value_adjusted"]].to_string())
