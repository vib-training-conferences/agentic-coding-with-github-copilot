# Extra exercise: Optimizing Code with GitHub Copilot Chat

## Learning Objective

Learn how to use GitHub Copilot Chat to identify performance bottlenecks and improve the efficiency of existing Python code. You will also learn to critically assess whether Copilot's suggested optimizations are correct and meaningful.

---

## Background

Researchers often write code that works correctly but runs slowly — especially on large datasets. Common problems include:
- Nested loops that can be replaced with vectorized operations
- Repeated computations that could be cached
- Inefficient data structures

GitHub Copilot Chat can suggest optimizations, but you should always:
1. **Benchmark** before and after to confirm the improvement
2. **Verify correctness** — an optimized function that gives wrong results is worse than a slow correct one

> **Key insight**: Copilot is good at recognizing common inefficiency patterns (e.g., Python loops that should use NumPy/Pandas). For domain-specific performance issues, you may need to guide it with more context.

---

## Exercise

The script below performs a differential expression analysis on gene expression data. It works correctly but is **unnecessarily slow** due to inefficient use of Python. Copy it into a new file (`optimize_exercise.py`) and use Copilot Chat to optimize it.

```python
import pandas as pd
import numpy as np
import time

def load_data(filepath):
    return pd.read_csv(filepath)

def compute_statistics_slow(df):
    """
    Compute mean, standard deviation, and log2 fold change for each gene.
    This implementation uses explicit Python loops — it works but is slow.
    """
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]

    results = []
    for idx in range(len(df)):
        row = df.iloc[idx]
        gene_id = row["gene_id"]
        gene_name = row["gene_name"]

        # Compute means using a Python loop instead of numpy
        ctrl_sum = 0
        for col in control_cols:
            ctrl_sum += row[col]
        ctrl_mean = ctrl_sum / len(control_cols)

        treat_sum = 0
        for col in treatment_cols:
            treat_sum += row[col]
        treat_mean = treat_sum / len(treatment_cols)

        # Compute standard deviations using a Python loop
        ctrl_sq_diff_sum = 0
        for col in control_cols:
            ctrl_sq_diff_sum += (row[col] - ctrl_mean) ** 2
        ctrl_std = (ctrl_sq_diff_sum / len(control_cols)) ** 0.5

        treat_sq_diff_sum = 0
        for col in treatment_cols:
            treat_sq_diff_sum += (row[col] - treat_mean) ** 2
        treat_std = (treat_sq_diff_sum / len(treatment_cols)) ** 0.5

        # Compute log2 fold change
        if ctrl_mean > 0:
            log2_fc = np.log2(treat_mean / ctrl_mean)
        else:
            log2_fc = np.nan

        results.append({
            "gene_id": gene_id,
            "gene_name": gene_name,
            "ctrl_mean": ctrl_mean,
            "treat_mean": treat_mean,
            "ctrl_std": ctrl_std,
            "treat_std": treat_std,
            "log2_fold_change": log2_fc
        })

    return pd.DataFrame(results)

def classify_genes_slow(results_df, fc_threshold=1.0, min_mean=10.0):
    """
    Classify genes as upregulated, downregulated, or unchanged.
    Uses explicit iteration instead of vectorized operations.
    """
    classifications = []
    for idx in range(len(results_df)):
        row = results_df.iloc[idx]
        fc = row["log2_fold_change"]
        mean_expr = (row["ctrl_mean"] + row["treat_mean"]) / 2

        if mean_expr < min_mean:
            classifications.append("low_expression")
        elif np.isnan(fc):
            classifications.append("undefined")
        elif fc > fc_threshold:
            classifications.append("upregulated")
        elif fc < -fc_threshold:
            classifications.append("downregulated")
        else:
            classifications.append("unchanged")

    results_df = results_df.copy()
    results_df["regulation"] = classifications
    return results_df


if __name__ == "__main__":
    df = load_data("../../data/gene_expression.csv")

    # Time the slow version
    start = time.time()
    results = compute_statistics_slow(df)
    results = classify_genes_slow(results)
    elapsed = time.time() - start

    print(f"Slow version took: {elapsed:.4f} seconds")
    print(results[["gene_name", "log2_fold_change", "regulation"]].head(10))
```

---

## Tasks

### Task 1: Profile the slow code

Run the script and note the execution time. For this small dataset the difference may be small, but imagine running the same logic on 20,000 genes — the pattern matters.

### Task 2: Ask Copilot to optimize

Use Copilot Chat with these prompts:

```
This Python function uses explicit for-loops to compute means and standard deviations on a pandas DataFrame. Can you rewrite it using vectorized pandas/numpy operations to make it faster?
```

```
Rewrite this function to use pandas vectorized operations instead of iterating row by row:
[paste classify_genes_slow function]
```

### Task 3: Benchmark and compare

After applying Copilot's optimizations:
1. Run both the original and optimized versions
2. Use `time.time()` or `timeit` to compare the execution times
3. Confirm that both versions produce **identical results** by comparing the output DataFrames

```python
# Tip: Check if two DataFrames are equal
pd.testing.assert_frame_equal(results_slow, results_fast, check_like=True)
```

---

## Reflection

1. **How much faster is the optimized version?** (The difference will be more dramatic on larger datasets — try duplicating the data 100× to see the effect)
2. **Was the optimized code correct?** Did you need to adjust Copilot's suggestion?
3. **Readability trade-off**: Is the optimized code harder to understand? How should you document it?
4. **When NOT to optimize**: Copilot might suggest complex optimizations that only marginally improve speed while making the code much harder to maintain. How do you decide when optimization is worth it?

---

## Extension (Optional)

Ask Copilot to generate a **larger synthetic dataset** (e.g., 10,000 genes with random expression values) and benchmark the two versions again to see a more dramatic difference.

```
Write a Python function that generates a synthetic gene expression DataFrame with n genes and 3 control and 3 treatment samples with random expression values drawn from a log-normal distribution.
```
