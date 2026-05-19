## Exercise 5: Defining Agent Skills

**Duration:** 15-30 minutes
**Goal:** In this exercise, you will create a custom GitHub Copilot Agent Skill that can orchestrate multiple scripts and terminal commands to perform a complex task.

GitHub Copilot Agent Skills allow you to define highly specific toolchains, scripts, and instructions that Copilot can automatically load and execute when relevant. Unlike simple prompt files, Skills are stored in a specific directory structure with a `SKILL.md` file and can be granted permission to run terminal commands to orchestrate real workflows.

***

In this exercise, we will create an agent skill that orchestrates our Python pipeline to analyze new DNA datasets.

1. Take a quick look at the sample DNA file located at `data/sample_dna.txt`.
2. In your workspace root, create a new directory for your skill: `.github/skills/sequence-analyzer/`.
3. Copy the three Python scripts (`01_transcribe.py`, `02_translate.py`, `03_analyze.py`) from `exercises/04_agentic_control/DNA_analysis_pipeline/` into this new `sequence-analyzer` directory. When a skill is invoked, Copilot makes all files in the skill's directory available alongside the instructions!
4. Inside of `sequence-analyzer`, create a file named `SKILL.md`. 
5. Add the following content to `SKILL.md`. Notice the YAML frontmatter which defines the skill's identity, metadata, and allowed tools:

   ```markdown
   ---
   name: sequence-analyzer
   description: Orchestrates running the bioinformatics pipeline scripts to transcribe, translate, and analyze DNA sequences. Use this when asked to analyze a DNA sequence.
   allowed-tools: shell
   ---
   
   When you are asked to analyze a DNA sequence, you must act autonomously by executing terminal commands to run the bioinformatics pipeline. Perform these steps in order:
   
   1. Read the input sequence from the provided file or context.
   2. Run the `01_transcribe.py` script provided in this skill's directory, passing the sequence as an argument.
   3. Take the output from step 2, and pass it as an argument to the `02_translate.py` script provided in this skill's directory.
   4. Take the output from step 3, and pass it as an argument to the `03_analyze.py` script provided in this skill's directory.
   
   Do not just give the user the code to run it themselves; use your shell execution abilities to run the commands and report the final analysis results.
   ```

6. Open Copilot Chat.
7. Trigger the skill by prompting Copilot with something that matches its description: *"Analyze the sequence in #file:sample_dna.txt"*.
8. Watch as Copilot automatically discovers the `sequence-analyzer` skill, adopts the instructions, understands the local Python scripts context, and executes the terminal commands step by step!

> Note: Depending on the model that you are using, you may need to explicitly mention the skill name in your prompt, e.g., *"Use the sequence-analyzer skill to analyze the sequence in #file:sample_dna.txt"*. Especially smaller and older models are less likely to call skills autonomously.

***

### Warning

Agent Skills are extremely powerful and can run any terminal command you allow them to. Always review the `SKILL.md` instructions and the files in the skill's directory before invoking it, especially if it's a skill you didn't create yourself.