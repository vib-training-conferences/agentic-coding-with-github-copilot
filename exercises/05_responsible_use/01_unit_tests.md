## Exercise: Unit Testing with GitHub Copilot

**Duration**: 10-15 minutes
**Goal**: Learn how to use GitHub Copilot to generate unit tests for your code, ensuring that it works correctly and reliably.

Writing code is only half the battle; ensuring it works reliably under various conditions is equally important. When using AI assistants like GitHub Copilot to write code, it is **crucial** to verify the output with unit tests to prevent hallucinations or logic errors from silently creeping into your software.

In this exercise, we will use the scripts from the previous section and generate unit tests for them using GitHub Copilot's built-in commands.

***

### Step 1: Prepare the Code
1. Open one of the scripts from the previous section, for example, `exercises/04_agentic_control/scripts/01_transcribe.py`.
2. Ensure the code is encapsulated in a function so it can be easily tested. If it's just a raw procedural script, use Copilot to quickly refactor it into a reusable function (e.g., `def transcribe(dna_sequence):`). 

> *Tip: highlight the code, open Copilot Chat (or inline chat with `Cmd+I` / `Ctrl+I`), and type: "Refactor this code into a function".*

***

### Step 2: Generate Tests with the `/tests` command
1. Highlight your newly created function.
2. In the Copilot Chat panel, type the `/tests` command. Copilot will automatically analyze your function and generate a suite of unit tests for it (using standard testing frameworks like `unittest` or `pytest`).
3. Review the generated tests in the chat. Are they checking edge cases (e.g., empty strings, unexpected characters)? Are they testing the expected "happy path" behavior?
4. Put the generated test code into a new file named `test_transcribe.py` in the same directory as your script.

***

### Step 3: Run and Evaluate the Tests
1. Open a new terminal in VS Code (`Terminal -> New Terminal`).
2. Run the tests using the appropriate testing framework. For example, if Copilot generated `unittest` tests, run:
   ```bash
   python -m unittest test_transcribe.py
   ```
   Or for `pytest` (if installed):
   ```bash
   pytest test_transcribe.py
   ```
3. Evaluate the results. Did all tests pass? If a test fails, this is a great opportunity to explore how Copilot can assist with debugging!

> *Note: you may need to add a __init__.py file to the scripts directory to ensure the tests can import the function correctly. If that doesn't work, you can also add the scripts directory to your Python path by adding this at the beginning of the test file:*
> ```python
> import sys
> import os
> sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts")))
> ```

> *Tip: You can directly include the terminal output into the Copilot Chat with #getTerminalOutput, and ask "Why is this test failing?".*
