"""
Solution 2.4: Fixed Debugging Script

This file contains all seven bugs from the exercise script fixed and annotated.
Each fix is marked with a comment explaining what was wrong and what was changed.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats


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

    # FIX 1: The condition was inverted. We should raise if values ARE negative,
    # so the condition must check for any value < 0 (not >= 0).
    expr_cols = ["ctrl_1", "ctrl_2", "ctrl_3", "treat_1", "treat_2", "treat_3"]
    if (df[expr_cols] < 0).any().any():
        raise ValueError("Expression values must be non-negative")

    return df


def compute_log2_fold_change(df, pseudocount=1.0):
    """Compute log2 fold change for each gene with a pseudocount to handle zeros."""
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]

    mean_ctrl = df[control_cols].mean(axis=1)
    mean_treat = df[treatment_cols].mean(axis=1)

    # FIX 2: Add a pseudocount to avoid log2(0) = -inf and division by zero.
    log2_fc = np.log2((mean_treat + pseudocount) / (mean_ctrl + pseudocount))

    result = df[["gene_id", "gene_name"]].copy()
    result["mean_ctrl"] = mean_ctrl
    result["mean_treat"] = mean_treat
    result["log2_fold_change"] = log2_fc
    return result


def compute_simple_pvalue(ctrl_values, treat_values):
    """
    Compute a two-tailed two-sample t-test p-value.
    Returns the p-value (float between 0 and 1).
    """
    ctrl_arr = np.array(ctrl_values, dtype=float)
    treat_arr = np.array(treat_values, dtype=float)

    n1 = len(ctrl_arr)
    n2 = len(treat_arr)

    mean1 = np.mean(ctrl_arr)
    mean2 = np.mean(treat_arr)

    var1 = np.var(ctrl_arr, ddof=1)
    var2 = np.var(treat_arr, ddof=1)

    se = np.sqrt(var1 / n1 + var2 / n2)
    # FIX 3: The formula was correct, but we now guard against se == 0
    # (which was already there) and ensure we use the correct t-distribution.

    if se == 0:
        return 1.0

    t_stat = (mean2 - mean1) / se

    # FIX 4: Use a two-tailed p-value. scipy.stats.norm.sf gives the one-tailed
    # probability; multiply by 2 for the two-tailed test. Also use the t-
    # distribution with appropriate degrees of freedom (Welch's approximation).
    df_welch = (var1 / n1 + var2 / n2) ** 2 / (
        (var1 / n1) ** 2 / (n1 - 1) + (var2 / n2) ** 2 / (n2 - 1)
    )
    p_value = 2 * stats.t.sf(abs(t_stat), df=df_welch)
    return float(p_value)


def add_pvalues(result_df, original_df):
    """Add p-values for each gene to the results DataFrame."""
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]

    pvalues = []
    for idx in result_df.index:
        gene_id = result_df.loc[idx, "gene_id"]

        # FIX 5: Use original_df (which has the raw expression columns) instead
        # of result_df (which only has means and fold changes).
        gene_row = original_df[original_df["gene_id"] == gene_id].iloc[0]

        ctrl_vals = gene_row[control_cols].values.tolist()
        treat_vals = gene_row[treatment_cols].values.tolist()

        pval = compute_simple_pvalue(ctrl_vals, treat_vals)
        pvalues.append(pval)

    result_df = result_df.copy()
    result_df["p_value"] = pvalues
    return result_df


def apply_multiple_testing_correction(result_df, method="bonferroni"):
    """Apply multiple testing correction to p-values."""
    n_tests = len(result_df)

    if method == "bonferroni":
        result_df = result_df.copy()
        adjusted = result_df["p_value"] * n_tests
        # FIX 6: Cap adjusted p-values at 1.0 — probabilities cannot exceed 1.
        result_df["p_value_adjusted"] = adjusted.clip(upper=1.0)
    else:
        raise ValueError(f"Unknown correction method: {method}")

    return result_df


def get_significant_genes(result_df, alpha=0.05, log2fc_threshold=1.0):
    """Return genes that are statistically significant and differentially expressed."""
    significant = result_df[
        (result_df["p_value_adjusted"] < alpha) &
        # FIX 7: Use absolute value of log2_fold_change to capture both
        # upregulated and downregulated genes.
        (result_df["log2_fold_change"].abs() > log2fc_threshold)
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
    if len(significant) > 0:
        print(significant[["gene_name", "log2_fold_change", "p_value", "p_value_adjusted"]].to_string())
    else:
        print("  (none at the current significance threshold — expected with n=3 replicates)")
