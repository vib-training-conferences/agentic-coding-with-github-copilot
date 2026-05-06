## Exercise: Manual agent loop with chat‑based coding

**Duration:** 10–15 minutes  
**Goal:** Experience both the power *and* the friction of chat‑based coding.

***

### Setup

- Students use **any chat‑based LLM** (ChatGPT, Copilot Chat, etc.)
- No IDE integration yet
- No automation

***

### Task

**Problem statement:**

> “Write a small Python script that reads a CSV file with two columns (`sample_id`, `value`), calculates the mean per sample, and writes the result to a new CSV file.”

***

### Step 1 — Plan (explicit)

Add this sentence to the prompt:

> “Before writing code, explain how you would approach this task step by step.”

***

### Step 2 — Act

Ask the model to generate the code. Copy the code into your editor (VS Code, Jupyter, etc.) and run it.

***

### Step 3 — Observe

Check the code for correctness and completeness:

*   Does it run?
*   Are edge cases handled?
*   Are assumptions documented?
*   Does it match *your* expectation of correctness?

***

### Step 4 — Reflect

Ask the model to revise the code based on your observations. For example:

> “Improve the code to handle empty files and add minimal documentation.”

You can also ask the model to help with this process:

> “What are some edge cases that might cause the code to fail? How would you fix them?”

> “Identify the weaknesses in the current implementation. How would you improve it?”

***

### Reflection (plenary discussion)

Ask yourself these questions:

*   Did everyone get the *same* code?
*   Did the code work immediately?
*   What context did the model not have?
*   Where did *you* need to intervene?
*   How much copy‑paste was involved?