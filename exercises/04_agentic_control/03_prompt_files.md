# Exercise 3: Reusable Prompt Files

Often, you'll perform the same code review or scaffolding tasks repeatedly. Prompt files let you save these instructions so you don't have to type them out every time.

1. Create a new file called `review-code.prompt.md` in the `.github/prompts` folder.
2. Add the following content to it:
   ```markdown
   ---
   name: review-code
   description: Review the selected code for edge cases in biological sequences.
   agent: ask
   ---
   Review the selected code for edge cases in biological sequences.
   Specifically check for:
   - Missing start or stop codons
   - Unknown characters
   - Sequence length not divisible by 3
   ```
3. Open `02_translate.py` and highlight the `translate` function.
4. In Copilot Chat, click the paperclip icon (Attach Context) and find your `review.prompt` file, or mention it in the chat box. Ask Copilot to run the prompt instructions on your `#selection`.
5. See what edge cases Copilot brings up and let it suggest fixes for them.