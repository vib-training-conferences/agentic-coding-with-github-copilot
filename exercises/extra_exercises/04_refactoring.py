"""
Extra exercise: Refactoring and Optimizing an Existing Script

This script performs a complete differential expression analysis pipeline.
It works correctly but has several code quality issues:
  - Code duplication
  - Magic numbers (unexplained literal values)
  - Long functions that do too many things
  - Inconsistent naming conventions
  - Missing error handling
  - Inefficient pandas operations

Your tasks:
  1. Read through the code to understand what it does
  2. Run the script to confirm it works
  3. Use GitHub Copilot to identify areas for improvement
  4. Refactor the code with Copilot's help
  5. Confirm the refactored script produces the same results

Useful prompts for Copilot:
  - "Identify code quality issues in this function: [paste function]"
  - "Refactor this function to follow the single-responsibility principle"
  - "Replace these magic numbers with named constants"
  - "This code is duplicated in two places. Extract it into a shared helper function."
  - "Rewrite these pandas operations more efficiently using vectorized operations"
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend
from pathlib import Path


def run_full_analysis(input_file, output_dir):
    # Read the data
    df = pd.read_csv(input_file)
    print(f"Loaded {len(df)} genes from {input_file}")

    # --- Normalize control samples ---
    # Compute per-sample scaling factors (normalize to 1 million total counts)
    ctrl_1_total = df["ctrl_1"].sum() + 1
    ctrl_2_total = df["ctrl_2"].sum() + 1
    ctrl_3_total = df["ctrl_3"].sum() + 1
    treat_1_total = df["treat_1"].sum() + 1
    treat_2_total = df["treat_2"].sum() + 1
    treat_3_total = df["treat_3"].sum() + 1

    df["ctrl_1_norm"] = (df["ctrl_1"] + 1) / ctrl_1_total * 1000000
    df["ctrl_2_norm"] = (df["ctrl_2"] + 1) / ctrl_2_total * 1000000
    df["ctrl_3_norm"] = (df["ctrl_3"] + 1) / ctrl_3_total * 1000000
    df["treat_1_norm"] = (df["treat_1"] + 1) / treat_1_total * 1000000
    df["treat_2_norm"] = (df["treat_2"] + 1) / treat_2_total * 1000000
    df["treat_3_norm"] = (df["treat_3"] + 1) / treat_3_total * 1000000

    # --- Compute means and fold change ---
    df["ctrl_mean"] = (df["ctrl_1_norm"] + df["ctrl_2_norm"] + df["ctrl_3_norm"]) / 3
    df["treat_mean"] = (df["treat_1_norm"] + df["treat_2_norm"] + df["treat_3_norm"]) / 3

    # Avoid log of zero by adding a small pseudocount
    df["log2_fc"] = np.log2((df["treat_mean"] + 0.001) / (df["ctrl_mean"] + 0.001))

    # --- Compute variability ---
    ctrl_norm_cols = ["ctrl_1_norm", "ctrl_2_norm", "ctrl_3_norm"]
    treat_norm_cols = ["treat_1_norm", "treat_2_norm", "treat_3_norm"]

    df["ctrl_std"] = df[ctrl_norm_cols].std(axis=1)
    df["treat_std"] = df[treat_norm_cols].std(axis=1)

    # Coefficient of variation (CV = std/mean)
    df["ctrl_cv"] = df["ctrl_std"] / (df["ctrl_mean"] + 0.001)
    df["treat_cv"] = df["treat_std"] / (df["treat_mean"] + 0.001)

    # --- Filter and classify genes ---
    # Keep only genes with sufficient expression
    expressed = df[df["ctrl_mean"] >= 10].copy()
    expressed = expressed[expressed["treat_mean"] >= 10].copy()

    # Classify as upregulated, downregulated, or unchanged
    expressed["regulation"] = "unchanged"
    expressed.loc[expressed["log2_fc"] >= 1, "regulation"] = "upregulated"
    expressed.loc[expressed["log2_fc"] <= -1, "regulation"] = "downregulated"

    n_up = len(expressed[expressed["regulation"] == "upregulated"])
    n_down = len(expressed[expressed["regulation"] == "downregulated"])
    n_unchanged = len(expressed[expressed["regulation"] == "unchanged"])

    print(f"\nResults after filtering (min expression = 10 CPM):")
    print(f"  Total expressed genes: {len(expressed)}")
    print(f"  Upregulated (log2FC >= 1): {n_up}")
    print(f"  Downregulated (log2FC <= -1): {n_down}")
    print(f"  Unchanged: {n_unchanged}")

    # --- Save results ---
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results_file = output_dir / "de_results.csv"
    expressed.to_csv(results_file, index=False)
    print(f"\nResults saved to {results_file}")

    # --- Create a simple bar chart of regulation counts ---
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ["Upregulated", "Downregulated", "Unchanged"]
    counts = [n_up, n_down, n_unchanged]
    colors = ["#d62728", "#1f77b4", "#aec7e8"]
    ax.bar(categories, counts, color=colors)
    ax.set_ylabel("Number of genes")
    ax.set_title("Differential Expression Summary")
    for i, v in enumerate(counts):
        ax.text(i, v + 0.1, str(v), ha="center", va="bottom")
    plt.tight_layout()
    bar_chart_file = output_dir / "de_summary_bar.png"
    plt.savefig(bar_chart_file, dpi=100)
    plt.close()
    print(f"Bar chart saved to {bar_chart_file}")

    # --- Create a volcano plot ---
    fig2, ax2 = plt.subplots(figsize=(8, 6))

    colors_volcano = []
    for _, row in expressed.iterrows():
        if row["regulation"] == "upregulated":
            colors_volcano.append("#d62728")
        elif row["regulation"] == "downregulated":
            colors_volcano.append("#1f77b4")
        else:
            colors_volcano.append("#aec7e8")

    # Use log2FC on x-axis and ctrl_cv as a proxy for variability on y-axis
    ax2.scatter(expressed["log2_fc"], expressed["ctrl_cv"], c=colors_volcano, alpha=0.7)
    ax2.axvline(x=1, color="gray", linestyle="--", linewidth=0.8)
    ax2.axvline(x=-1, color="gray", linestyle="--", linewidth=0.8)
    ax2.set_xlabel("log2 Fold Change")
    ax2.set_ylabel("Coefficient of Variation (Control)")
    ax2.set_title("Volcano-style plot: Fold Change vs. Variability")

    # Label top 5 upregulated and top 5 downregulated
    top_up = expressed[expressed["regulation"] == "upregulated"].nlargest(5, "log2_fc")
    top_down = expressed[expressed["regulation"] == "downregulated"].nsmallest(5, "log2_fc")

    for _, row in top_up.iterrows():
        ax2.annotate(row["gene_name"], (row["log2_fc"], row["ctrl_cv"]),
                     fontsize=7, ha="left", va="bottom")
    for _, row in top_down.iterrows():
        ax2.annotate(row["gene_name"], (row["log2_fc"], row["ctrl_cv"]),
                     fontsize=7, ha="right", va="bottom")

    plt.tight_layout()
    volcano_file = output_dir / "volcano_plot.png"
    plt.savefig(volcano_file, dpi=100)
    plt.close()
    print(f"Volcano plot saved to {volcano_file}")

    return expressed


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    data_file = script_dir.parent.parent / "data" / "gene_expression.csv"
    output_directory = script_dir / "output"

    results = run_full_analysis(data_file, output_directory)
