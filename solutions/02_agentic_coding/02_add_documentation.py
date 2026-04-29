"""
Solution 2.2: Adding Documentation to Existing Functions

This file demonstrates a fully documented version of the exercise script.
Documentation follows NumPy docstring style.
"""

import numpy as np
import pandas as pd
from typing import Optional


def normalize_expression(df: pd.DataFrame, method: str = "tpm", pseudocount: float = 1.0) -> pd.DataFrame:
    """
    Normalize gene expression values across samples.

    Applies one of three normalization strategies to the expression columns
    in the input DataFrame. Control columns are identified by the prefix
    ``ctrl`` and treatment columns by the prefix ``treat``.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing gene metadata and raw expression values.
        Must include columns whose names start with ``ctrl`` or ``treat``.
    method : str, optional
        Normalization method to apply. One of:
        - ``"tpm"``    : Transcripts Per Million — scales each column so that
                         the total (plus pseudocount) equals 1 × 10⁶.
        - ``"log2"``   : Log2 transformation with pseudocount addition.
        - ``"zscore"`` : Z-score standardisation per column (mean 0, std 1).
        Default is ``"tpm"``.
    pseudocount : float, optional
        Small value added to expression counts before transformation to avoid
        log(0) and division-by-zero errors. Default is ``1.0``.

    Returns
    -------
    pd.DataFrame
        A copy of ``df`` with expression columns replaced by normalised values.
        All other columns (metadata) are unchanged.

    Raises
    ------
    ValueError
        If ``method`` is not one of the supported normalization strategies.

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
    ...     "gene_id": ["G1", "G2"],
    ...     "ctrl_1": [100.0, 200.0],
    ...     "treat_1": [150.0, 50.0],
    ... })
    >>> normalized = normalize_expression(data, method="log2")
    >>> normalized["ctrl_1"].tolist()  # log2(100 + 1) ≈ 6.66
    [6.658211482751793, 7.651051691178929]
    """
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
        raise ValueError(f"Unknown normalization method: {method!r}. "
                         f"Choose from 'tpm', 'log2', or 'zscore'.")

    return result


def compute_differential_expression(df: pd.DataFrame, min_expression: float = 1.0) -> pd.DataFrame:
    """
    Compute differential expression statistics between control and treatment groups.

    For each gene, calculates group means, standard deviations, and the
    log2 fold change (log2(mean_treatment / mean_control)).  Genes whose
    mean control expression is below ``min_expression`` receive ``NaN`` for
    the fold change to avoid spurious results driven by low-count noise.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with columns starting with ``ctrl`` (control samples) and
        ``treat`` (treatment samples), plus ``gene_id`` and ``gene_name``.
    min_expression : float, optional
        Minimum mean control expression required to compute a fold change.
        Genes below this threshold are assigned ``NaN``. Default is ``1.0``.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with one row per gene and the following columns:

        - ``gene_id``          : Gene identifier from the input DataFrame.
        - ``gene_name``        : Gene name from the input DataFrame.
        - ``mean_ctrl``        : Mean expression across control replicates.
        - ``mean_treat``       : Mean expression across treatment replicates.
        - ``std_ctrl``         : Standard deviation across control replicates.
        - ``std_treat``        : Standard deviation across treatment replicates.
        - ``log2_fold_change`` : log2(mean_treat / mean_ctrl), or ``NaN`` if
                                 ``mean_ctrl < min_expression``.
        - ``se``               : Standard error of the fold change estimate
                                 (propagated from within-group variances).
    """
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


def filter_genes(
    result_df: pd.DataFrame,
    log2fc_threshold: float = 1.0,
    min_mean_expression: float = 10.0,
) -> pd.DataFrame:
    """
    Filter differentially expressed genes by fold change and minimum expression.

    Retains only genes whose absolute log2 fold change meets or exceeds
    ``log2fc_threshold`` **and** whose average expression (mean of control and
    treatment group means) is at least ``min_mean_expression``.  The output is
    sorted by log2 fold change in descending order (most upregulated first).

    Parameters
    ----------
    result_df : pd.DataFrame
        Output of :func:`compute_differential_expression`.  Must contain
        columns ``log2_fold_change``, ``mean_ctrl``, and ``mean_treat``.
    log2fc_threshold : float, optional
        Minimum absolute log2 fold change for a gene to be considered
        differentially expressed. Default is ``1.0`` (i.e., a 2-fold change).
    min_mean_expression : float, optional
        Minimum average expression (arithmetic mean of the two group means)
        required for a gene to be retained. Default is ``10.0``.

    Returns
    -------
    pd.DataFrame
        Filtered and sorted copy of ``result_df`` with a reset index.
        Genes with ``NaN`` log2 fold change are excluded.
    """
    abs_fc = result_df["log2_fold_change"].abs()
    mean_expr = (result_df["mean_ctrl"] + result_df["mean_treat"]) / 2

    mask = (abs_fc >= log2fc_threshold) & (mean_expr >= min_mean_expression)
    filtered = result_df[mask].copy()
    filtered = filtered.sort_values("log2_fold_change", ascending=False)
    filtered = filtered.reset_index(drop=True)

    return filtered


def summarize_de_results(result_df: pd.DataFrame, log2fc_threshold: float = 1.0) -> dict:
    """
    Summarize differential expression results.

    Counts the number of upregulated, downregulated, and unchanged genes
    relative to the given fold change threshold, and identifies the gene
    with the largest positive and the largest negative fold change.

    Parameters
    ----------
    result_df : pd.DataFrame
        DataFrame with a ``log2_fold_change`` column (e.g., the output of
        :func:`compute_differential_expression` or :func:`filter_genes`).
        Rows with ``NaN`` fold change are excluded from the counts.
    log2fc_threshold : float, optional
        Absolute log2 fold change threshold used to classify genes as
        upregulated or downregulated. Default is ``1.0``.

    Returns
    -------
    dict
        Dictionary with the following keys:

        - ``"total_genes_analysed"``   : int — genes with a non-NaN fold change.
        - ``"upregulated"``            : int — genes with log2FC > threshold.
        - ``"downregulated"``          : int — genes with log2FC < −threshold.
        - ``"unchanged"``              : int — remaining genes.
        - ``"top_upregulated_gene"``   : str — gene name with highest log2FC
                                         (only present if upregulated > 0).
        - ``"top_downregulated_gene"`` : str — gene name with lowest log2FC
                                         (only present if downregulated > 0).
    """
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


def compute_correlation_matrix(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """
    Compute the inter-sample correlation matrix for expression data.

    Transposes the expression sub-matrix so that samples become rows and genes
    become columns, then computes pairwise correlations between samples.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing expression columns prefixed with ``ctrl`` or
        ``treat``. Non-expression columns are ignored.
    method : str, optional
        Correlation method to use. Passed directly to
        :meth:`pandas.DataFrame.corr`. One of ``"pearson"``, ``"kendall"``,
        or ``"spearman"``. Default is ``"pearson"``.

    Returns
    -------
    pd.DataFrame
        Square correlation matrix of shape (n_samples, n_samples) where
        rows and columns are labelled with sample names.

    Examples
    --------
    >>> corr = compute_correlation_matrix(df, method="spearman")
    >>> corr.shape
    (6, 6)
    """
    control_cols = [c for c in df.columns if c.startswith("ctrl")]
    treatment_cols = [c for c in df.columns if c.startswith("treat")]
    sample_cols = control_cols + treatment_cols

    expr_matrix = df[sample_cols].T
    corr_matrix = expr_matrix.corr(method=method)

    return corr_matrix
