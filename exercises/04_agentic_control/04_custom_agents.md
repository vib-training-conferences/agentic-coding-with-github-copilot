## Exercise 4: Defining Custom Agents

**Duration:** 15-30 minutes
**Goal:** In this exercise, we will learn how to create custom agents in GitHub Copilot.

While prompt files can act as simple slash commands (like `/review`), we can also create full **Custom Agents**. An agent (often invoked with an `@` mention like `@biocritic`) acts as a dedicated participant in the chat. It doesn't just inject text; it can be given a specific persona, instructions, and given access to specialized tools and context.

***

**Problem statement:**

In this exercise we will create a custom agent called `@biocritic` that specializes in reviewing bioinformatics code for biological correctness and efficiency. We will then create a second agent, `@bioengineer`, that takes the critic's feedback and implements the necessary code changes.

***

### 1. Creating a Custom Agent (@biocritic)

1. In your workspace root, create a directory named `.github/agents` (if you haven't already).
2. Inside that folder, create a new file named `biocritic.md`.
3. Add the following agent configuration to the file. Note how we define not just instructions, but the agent's *behavior* and *goals*:
   ```markdown
   ---
   name: biocritic
   description: An expert bioinformatics code reviewing agent
   ---

   You are @biocritic, an autonomous bioinformatics agent.
   Your goal is to ensure all biological scripts are robust, fast, and scientifically accurate.

   When asked to review code, you must independently:
   1. Analyze the biological correctness of sequence handling.
   2. Propose fixes for any inefficient memory usage (especially for large FASTA/FASTQ files).
   3. Provide a structured report with a "Severity" level for any issues found.
   ```
4. Open the chat. Notice that depending on your VS Code/Copilot version, this prompt might now be available as an explicitly named custom agent or participant (e.g., by typing `@biocritic` or by selecting it from the agent dropdown).
5. Open `scripts/01_transcribe.py`.
6. Ask your new agent: `@biocritic analyze the #selection for a pipeline that processes 3GB of data.`
7. Observe how the agent embodies the persona and strictly follows the structured reporting format defined in its configuration.

***

### 2. Agent Hand-offs (@biocritic -> @bioengineer)

To truly leverage agentic workflows, you can string different specialized agents together. Let's create a builder agent that takes the critic's feedback and writes the updated code.

1. In the `.github/agents/` directory, create another file named `bioengineer.md`.
2. Add the following configuration to `bioengineer.md`:
   ```markdown
   ---
   name: bioengineer
   description: An expert bioinformatics software engineer
   ---

   You are @bioengineer. Your job is to write and fix python code based on code review reports. 
   
   When given a review report from @biocritic:
   1. Implement all critical and major fixes.
   2. Always use streaming/generators for large sequence processing.
   3. Output the complete, refactored python script.
   ```
3. In your active chat where `@biocritic` just finished its review, directly ask your new agent: `@bioengineer Please rewrite the #selection based on the recommendations from @biocritic above.`
4. Watch as Copilot uses the context of the previous agent's output to perform a seamless hand-off and generates the fully corrected pipeline script!

We can also make this hand-off more explicit in the YAML front matter of `biocritic.md` to ensure that whenever `@biocritic` finishes a review, it automatically triggers `@bioengineer` to implement the changes.

5. Edit the `biocritic.md` file to include a hand-off instruction:
```markdown
---
name: biocritic
description: An expert bioinformatics code reviewing agent
handoff:
    - label: Implement Plan
      agent: bioengineer
      prompt: Implement the plan outlined above
      send: false
---
```
6. Start a new chat and ask `@biocritic` to review the code again. After it provides the structured report, you should see an option to trigger the hand-off to `@bioengineer` directly from the chat interface, streamlining the workflow from review to implementation.

