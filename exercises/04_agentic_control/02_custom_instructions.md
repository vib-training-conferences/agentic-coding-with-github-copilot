# Exercise 2: Setting Rules with Custom Instructions

You can give Copilot a personality or set strict organizational coding rules. Let's force it to always write clean, documented CLI tools.

1. Create a file called `.github/copilot-instructions.md` in the root of the workspace (you may need to create the `.github` directory first).
2. Add this rule to the file: 
   `Always use argparse for command-line arguments. Always include numpy-style docstrings for functions.`
3. Open `scripts/01_transcribe.py`. Notice how it is currently very basic and strictly hardcoded.
4. Select all the code in that file, open Copilot Chat, and ask: *"Rewrite this script to take the DNA sequence as an input."*
5. Check the suggested code. Copilot should automatically use `argparse` and add docstrings, even though you didn't explicitly ask for those features in your prompt.