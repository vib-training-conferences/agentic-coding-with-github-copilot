## Exercise 1: Context is King

**Duration:** 5-10 minutes
**Goal:** In this exercise, we will see how providing context to GitHub Copilot can significantly improve its performance.

***

We will use the scripts in the `DNA_analysis_pipeline/` folder for this exercise.

1. Open `02_translate.py` and `03_analyze.py`.
2. In the chat, ask: *"How do `#file:02_translate.py` and `#file:03_analyze.py` interact?"* Notice how directly referencing the files gives a much better answer than just asking a generic question like "how do my protein scripts work?".
3. Now open a terminal and run `python exercises/04_agentic_control/scripts/03_analyze.py MARN*`. It will crash with a `TypeError`.
4. Select the `analyze` function code in `03_analyze.py`. In the chat, use `#selection` and `#terminalLastCommand` (or paste the error) and ask Copilot to fix the bug.