# Exercise 1.2: Debugging with GitHub Copilot Chat

## Learning Objective

Learn how to use GitHub Copilot Chat to identify and fix bugs in Python code. You will practice providing good context to Copilot and critically evaluating its suggestions.

---

## Background

Debugging is one of the most time-consuming parts of coding. Copilot Chat can help by:
- Identifying the cause of an error message
- Explaining what a piece of code does (and why it might be wrong)
- Suggesting fixes

> **Key insight**: Copilot understands error messages and stack traces very well. Pasting the error message together with the relevant code into Copilot Chat gives much better results than describing the problem in vague terms.

---

## Exercise

The following Python script is supposed to analyse gene expression data but contains **several bugs**. Copy the script into a new file (`debug_exercise.py`) in VS Code, then use **Copilot Chat** to identify and fix each bug.

```python
import pandas as pd
import numpy as np

def load_expression_data(filepath):
    """Load gene expression data from a CSV file."""
    df = pd.read_csv(filepath)
    return df

def calculate_fold_change(control_values, treatment_values):
    """Calculate log2 fold change between treatment and control."""
    # Bug 1: This calculation is wrong
    mean_control = np.mean(control_values)
    mean_treatment = np.mean(treatment_values)
    fold_change = mean_treatment - mean_control  # Should be log2(treatment/control)
    return fold_change

def filter_significant_genes(df, fold_change_threshold=1.0, min_expression=10):
    """Filter genes by fold change threshold and minimum expression."""
    control_cols = ["ctrl_1", "ctrl_2", "ctrl_3"]
    treatment_cols = ["treat_1", "treat_2", "treat_3"]
    
    fold_changes = []
    for i in df.index:
        ctrl = df.loc[i, control_cols].values
        treat = df.loc[i, treatment_cols].values
        fc = calculate_fold_change(ctrl, treat)
        fold_changes.append(fc)
    
    df["log2_fold_change"] = fold_changes
    
    # Bug 2: The filter logic uses OR instead of AND
    significant = df[
        (abs(df["log2_fold_change"]) > fold_change_threshold) |
        (df[control_cols].mean(axis=1) > min_expression)
    ]
    return significant

def get_top_genes(df, n=10):
    """Return the top n genes by absolute fold change."""
    # Bug 3: sort_values sorts in ascending order by default
    df_sorted = df.sort_values("log2_fold_change", ascending=True)
    return df_sorted.head(n)

def summarize_results(df):
    """Print a summary of the differential expression results."""
    n_up = len(df[df["log2_fold_change"] > 0])
    n_down = len(df[df["log2_fold_change"] < 0])
    
    print(f"Total significant genes: {len(df)}")
    print(f"Upregulated: {n_up}")
    print(f"Downregulated: {n_down}")
    
    # Bug 4: This will fail if df is empty
    print(f"Most upregulated gene: {df.sort_values('log2_fold_change').iloc[-1]['gene_name']}")
    print(f"Most downregulated gene: {df.sort_values('log2_fold_change').iloc[0]['gene_name']}")


if __name__ == "__main__":
    # Load data - update path as needed
    data = load_expression_data("../../data/gene_expression.csv")
    
    # Run analysis
    significant_genes = filter_significant_genes(data)
    top_genes = get_top_genes(significant_genes, n=10)
    summarize_results(top_genes)
```

---

## Tasks

### Task 1: Find the bugs manually

Read through the code carefully before using Copilot. Can you spot the **four bugs**? Write them down.

### Task 2: Use Copilot Chat to debug

1. Open Copilot Chat (`Ctrl+Alt+I`)
2. Run the script and paste the **error message** (or describe the unexpected behaviour) into the chat
3. Ask Copilot to explain the issue and suggest a fix

**Useful prompts to try:**
```
I have a bug in my Python function. Here is the code and the error I get: [paste code and error]. What is wrong and how do I fix it?
```
```
Review this function for logical errors: [paste function]
```
```
This function is supposed to return the top genes by absolute fold change, but the results look wrong. What might be the issue?
```

### Task 3: Fix and verify

Apply Copilot's suggested fixes and run the corrected script. Verify that:
- `calculate_fold_change` returns the correct log2 fold change
- `filter_significant_genes` only returns genes that pass **both** thresholds
- `get_top_genes` returns genes sorted by **absolute** fold change in **descending** order
- `summarize_results` handles empty DataFrames gracefully

---

## Reflection

1. **Which debugging approach was faster** — reading the code yourself or using Copilot Chat? Why?
2. **Did Copilot find all four bugs?** Did it find any issues you missed?
3. **Were Copilot's suggested fixes correct?** Did you need to modify them?
4. **Limitation**: What kinds of bugs is Copilot **less** good at detecting? (Think about domain-specific logic errors vs. syntax errors.)

---

## Extension (Optional)

Ask Copilot to write **unit tests** for the fixed functions using `pytest`. Then run the tests to confirm the fixes are correct.

```
Write pytest unit tests for the `calculate_fold_change` function, including tests for normal cases, edge cases (e.g., zero control mean), and expected exceptions.
```
