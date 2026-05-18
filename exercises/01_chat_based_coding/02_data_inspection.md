## Exercise: Data Analysis with Uploaded Files in Chat

**Duration:** 10–15 minutes
**Goal:** This exercise demonstrates that chat‑based LLMs can work directly with user‑provided data (e.g. CSV files) and perform exploratory data analysis *inside the chat interface*.

***

### Setup

- Use a chat‑based LLM that supports **file uploads** (e.g. ChatGPT, Copilot Chat with attachments)
- No IDE or local environment required
- Use a **non‑sensitive dataset only**. You can use the Teen_Mental_Health_Dataset.csv provided in the course materials (in the data folder).

***

### Step 1 — Upload and inspect

After uploading the file, ask:

**Prompt example:**

    Please load the uploaded CSV file and summarize its structure.

#### What to observe

- Does the model correctly infer columns and data types?
- Does it restate the data accurately?

***

### Step 2 — Basic exploratory analysis

Ask the model to perform simple analysis.

**Prompt example:**

    Calculate basic summary statistics per condition and explain what you observe.

Possible outputs:

- Means per group
- Counts
- Simple comparisons

***

### Step 3 — Visualization (conceptual)

Ask for a plot description or generated visualization.

**Prompt example:**

    Create a plot comparing the distributions of values between conditions and explain it.

#### What to observe

- Is the plot reasonable?
- Are assumptions stated?
- Does the explanation match the data?

***

### Reflection (Plenary Discussion)

- Where is the data actually processed?
- Can you reproduce this analysis exactly later?
- Is the analysis version‑controlled?
- Would you upload unpublished research data this way?
- How does this compare to running the same analysis locally?
