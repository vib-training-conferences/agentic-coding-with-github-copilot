# Exploring GitHub Copilot Features

In this exercise, we will explore the different features of GitHub Copilot.

You are given an unfinished pipeline from a former PhD student. Your task is to use Copilot to understand, complete, and improve the pipeline.

## 1. Ask Mode - Understand the context
Use the Copilot Chat panel to ask about the content of the current workspace directory. 
**Task:** Open the chat and ask what the purpose is of the scripts in the 'scripts' directory. Switch to the agent mode and ask Copilot to rename the scripts to be more descriptive of their function.

> Optional: You can also ask Copilot to generate a README file for this project that explains the purpose of each script and how they work together.

## 2. Ask Mode - Code Explanation
You can highlight specific code to have Copilot explain it.
**Task:** Open `script1.py` and highlight one of the functions. Ask Copilot to explain how it works. Review the explanation and ask follow-up questions if needed.

## 3. Edit - Add Documentation
**Task:** Open the script for reading alignments. Notice there are no docstrings for the functions. Highlight the functions and ask Copilot to generate docstrings. Use two different prompts:
- Prompt 1: "Document this script"
- Prompt 2: "Add concise docstrings to all functions, explain inputs/outputs, and keep comments beginner-friendly."

How do the generated docstrings differ between the two prompts? Which one do you find more useful?

> Optional: You can also ask Copilot to generate docstrings in a specific style. Ask Copilot to generate Google-style docstrings, NumPy-style docstrings, or reStructuredText-style docstrings. Compare the outputs and see which style you prefer.

## 4. Agent - Debugging
One of the files contains an intentional bug (modifying a dictionary while iterating over it).
**Task:** Open Copilot Chat in Agent mode and ask Copilot to identify and fix the bug. Example prompt: "Identify any bugs in this code and suggest a fix." Review the suggested fix and ask follow-up questions if needed.

## 5. Agent - Building the Pipeline
Now that we have the individual components, we need a main script to run them all.
**Task:** Ask Copilot to create a new script named `main.py` that imports all the functions from the other scripts, creates a small synthetic reference sequence and some synthetic reads, and runs the entire pipeline end-to-end (parsing, alignment, variant calling, filtering, and writing VCF).

## 6. Agent - Code Translation
**Task:** Ask Copilot to translate the entire pipeline to R or C++. See how it maps language-specific features (like generators vs lists). How confident are you in the translated code? Do you understand all the changes that were made during translation?

## 7. Plan - Future Improvements
**Task:** Use Copilot Chat's Plan feature to ask for ways to optimize or expand this pipeline. Example prompt: `Plan 3 new features to add to this variant calling pipeline for a subsequent exercise.`
