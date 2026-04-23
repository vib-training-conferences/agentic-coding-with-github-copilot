"""
Exercise 2.2: Adding Documentation to Existing Functions

In this exercise, you will use GitHub Copilot to add documentation to
undocumented Python functions. Documentation includes:
  - Module-level docstrings
  - Function-level docstrings (parameters, return values, exceptions, examples)
  - Inline comments for complex logic

Instructions:
  1. Open this file in VS Code
  2. For each function, place your cursor inside the function body
  3. Use Copilot Chat (Ctrl+Alt+I) or inline chat (Ctrl+I) to generate documentation
  4. Review and improve the generated documentation

Useful prompts:
  - "Add a NumPy-style docstring to this function"
  - "Add a Google-style docstring to this function, including parameter types,
     return type, and an example"
  - "Explain what this function does and add inline comments to complex lines"

After completing the exercise, your file should be fully documented and a reader
should be able to understand each function without reading the implementation.
"""

import numpy as np
import pandas as pd
from typing import Optional


def normalize_expression(df, method="tpm", pseudocount=1.0):
    control_cols = [c for c in df.columns if c.startswith("ctrl")]
    treatment_cols = [c for c in df.columns if c.startswith("treat")]
    expr_cols = control_cols + treatment_cols

    if method == "tpm":
        result = df.copy()
        for col in expr_cols:
            total = df[col].sum() + pseudocount
            result[col] = (df[col] + pseudocount) / total * 1e6
    elif method == "log2":
        result = df.copy()
        for col in expr_cols:
            result[col] = np.log2(df[col] + pseudocount)
    elif method == "zscore":
        result = df.copy()
        for col in expr_cols:
            mean = df[col].mean()
            std = df[col].std()
            if std == 0:
                result[col] = 0.0
            else:
                result[col] = (df[col] - mean) / std
    else:
        raise ValueError(f"Unknown normalization method: {method}")

    return result


def compute_differential_expression(df, min_expression=1.0):
    control_cols = [c for c in df.columns if c.startswith("ctrl")]
    treatment_cols = [c for c in df.columns if c.startswith("treat")]

    result = df[["gene_id", "gene_name"]].copy()

    result["mean_ctrl"] = df[control_cols].mean(axis=1)
    result["mean_treat"] = df[treatment_cols].mean(axis=1)
    result["std_ctrl"] = df[control_cols].std(axis=1)
    result["std_treat"] = df[treatment_cols].std(axis=1)

    mask = result["mean_ctrl"] >= min_expression
    result["log2_fold_change"] = np.nan
    result.loc[mask, "log2_fold_change"] = np.log2(
        result.loc[mask, "mean_treat"] / result.loc[mask, "mean_ctrl"]
    )

    n_ctrl = len(control_cols)
    n_treat = len(treatment_cols)
    result["se"] = np.sqrt(
        result["std_ctrl"] ** 2 / n_ctrl + result["std_treat"] ** 2 / n_treat
    )

    return result


def filter_genes(result_df, log2fc_threshold=1.0, min_mean_expression=10.0):
    abs_fc = result_df["log2_fold_change"].abs()
    mean_expr = (result_df["mean_ctrl"] + result_df["mean_treat"]) / 2

    mask = (abs_fc >= log2fc_threshold) & (mean_expr >= min_mean_expression)
    filtered = result_df[mask].copy()
    filtered = filtered.sort_values("log2_fold_change", ascending=False)
    filtered = filtered.reset_index(drop=True)

    return filtered


def summarize_de_results(result_df, log2fc_threshold=1.0):
    total = len(result_df.dropna(subset=["log2_fold_change"]))
    upregulated = (result_df["log2_fold_change"] > log2fc_threshold).sum()
    downregulated = (result_df["log2_fold_change"] < -log2fc_threshold).sum()
    unchanged = total - upregulated - downregulated

    summary = {
        "total_genes_analysed": total,
        "upregulated": int(upregulated),
        "downregulated": int(downregulated),
        "unchanged": int(unchanged),
    }

    if upregulated > 0:
        top_up = result_df[result_df["log2_fold_change"] > log2fc_threshold].nlargest(
            1, "log2_fold_change"
        )
        summary["top_upregulated_gene"] = top_up["gene_name"].values[0]

    if downregulated > 0:
        top_down = result_df[
            result_df["log2_fold_change"] < -log2fc_threshold
        ].nsmallest(1, "log2_fold_change")
        summary["top_downregulated_gene"] = top_down["gene_name"].values[0]

    return summary


def compute_correlation_matrix(df, method="pearson"):
    control_cols = [c for c in df.columns if c.startswith("ctrl")]
    treatment_cols = [c for c in df.columns if c.startswith("treat")]
    sample_cols = control_cols + treatment_cols

    expr_matrix = df[sample_cols].T
    corr_matrix = expr_matrix.corr(method=method)

    return corr_matrix
