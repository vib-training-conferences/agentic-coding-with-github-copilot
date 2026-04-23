# Exercise 1.4: Data Analysis with GitHub Copilot Chat

## Learning Objective

Learn how to use GitHub Copilot Chat (or ChatGPT) as a data analysis assistant. You will upload or describe a dataset and use Copilot to plan, execute, and visualize a data analysis workflow.

---

## Background

Modern LLMs can assist with the full data analysis cycle:
1. **Understanding the data**: exploring structure, checking for missing values, summarising distributions
2. **Analysis planning**: suggesting appropriate statistical methods
3. **Visualization**: generating plotting code
4. **Statistical testing**: running appropriate tests and interpreting results

> **Key insight**: Copilot and ChatGPT are powerful tools for exploratory data analysis, but they may suggest inappropriate statistical methods if they don't know your experimental design. Always describe your data and experimental context clearly.

---

## Dataset

Use the file `data/gene_expression.csv` from this repository. It contains:
- Gene metadata: `gene_id`, `gene_name`, `chromosome`, `gene_type`, `description`
- Expression values for 3 control samples: `ctrl_1`, `ctrl_2`, `ctrl_3`
- Expression values for 3 treatment samples: `treat_1`, `treat_2`, `treat_3`

The data represents RNA-seq-like expression measurements for ~40 cancer-related genes, with samples from an untreated control group and a drug-treated group.

---

## Exercise

### Option A: Using Copilot Chat in VS Code

Open a new Jupyter notebook (`data_analysis.ipynb`) in VS Code and use Copilot Chat to guide your analysis.

### Option B: Using ChatGPT

Navigate to [https://chatgpt.com](https://chatgpt.com), upload the CSV file, and use the conversation to explore the data.

---

## Tasks

Work through the following analysis steps by asking Copilot/ChatGPT to generate code or analysis for each one.

### Step 1: Load and Explore the Data

**Prompt:**
```
I have a gene expression dataset with the following columns: gene_id, gene_name, chromosome, gene_type, description, ctrl_1, ctrl_2, ctrl_3, treat_1, treat_2, treat_3. Write Python code to load this CSV file, display the first few rows, check for missing values, and print basic summary statistics.
```

Run the code and answer:
- How many genes are in the dataset?
- Are there any missing values?
- What is the range of expression values?

---

### Step 2: Visualize Expression Distributions

**Prompt:**
```
Write Python code using matplotlib and seaborn to create:
1. A histogram of all expression values across all samples
2. A boxplot comparing the distribution of expression values between control and treatment groups
3. A violin plot showing the same comparison
```

Discuss with a neighbour: What do these plots tell you about the data?

---

### Step 3: Calculate Differential Expression

**Prompt:**
```
Write Python code to calculate the log2 fold change (log2(mean_treatment / mean_control)) and the coefficient of variation for each gene. Add these as new columns to the DataFrame and display the top 10 most differentially expressed genes.
```

---

### Step 4: Visualize Differential Expression

**Prompt:**
```
Write Python code to create a volcano plot of the gene expression data. On the x-axis show the log2 fold change, and on the y-axis show the -log10 of a simple t-test p-value between the control and treatment groups. Highlight genes with |log2FC| > 1 in a different color and label the top 5 most significant genes.
```

> **Note**: The dataset is small (40 genes, 3 replicates) so statistical power will be low. This is intentional — it mirrors realistic small-scale experiments.

---

### Step 5: Ask Copilot to Suggest Further Analyses

Once you have the basics working, ask a more open-ended question:

**Prompt:**
```
Given this gene expression dataset comparing control vs treatment groups, what further analyses would you recommend? I'm particularly interested in understanding which biological pathways might be affected by the treatment.
```

Critically evaluate the suggestions:
- Are they appropriate for this dataset size?
- Do they require additional data or tools?
- Which suggestions are most useful for a first pass?

---

## Reflection

1. **How useful was Copilot/ChatGPT** as a data analysis assistant? Where did it shine and where did it struggle?
2. **Did you need to correct any of the generated code?** What was wrong?
3. **Statistical appropriateness**: With only 3 replicates per group, what are the limitations of the statistical tests suggested by Copilot?
4. **The "black box" problem**: If you had just run Copilot's code without understanding it, would you have caught any mistakes? What does this tell you about using AI for data analysis?

---

## Tips for Effective Data Analysis with Copilot

- **Describe your experimental design** explicitly (e.g., "These are biological replicates of RNA-seq data")
- **Iterate**: Start with simple analyses and build up
- **Always inspect intermediate outputs** — don't just run the full pipeline at once
- **Ask Copilot to explain** any function it uses that you don't recognize
- **Verify statistical results** against known literature or expected outcomes
