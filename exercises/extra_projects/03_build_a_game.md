# Exercise: Build a Game

The instinct after installing GitHub Copilot is to point it at the most important thing on your plate: the dashboard you have been meaning to rebuild, the workflow you want to automate, the strategy doc you have been putting off. Don’t. The first thing you build with a new tool should be small, fun, and disposable, because that is how you learn what the tool can actually do without your stakes clouding the lesson.

## Why a Game
Most people pick the wrong first project. They open Copilot with a real problem in mind, the agent runs for ten minutes, the result is rough around the edges, they conclude the tool is not ready. The conclusion is wrong; the first project was wrong.

A game is the right first project for three reasons:

1. **The model knows games.** Flappy Bird, Wordle, Snake, Tetris, a top-down RPG. The form is in the training data ten thousand times over. You provide a single sentence; the model fills in the rules, physics, styling, win condition. The first try is good.
2. **You can tell instantly if it works.** A game either feels playable or it doesn’t. There is no internal review loop, no “let me check with finance.” You open the file, you click around, you know.
3. **The stakes are zero.** Nothing depends on this. You can throw it away. Which means you can be brave with the prompt (silly, weird, specific) in a way you never quite are when the output is for real.
4. **Everything you learn here transfers.** The plan-execute loop, the make-it-better iteration, the way you steer the agent with one sentence instead of ten: those are the same moves you reach for later on the dashboard or the inbox automation. You learn them faster on something you do not care about.

## Warning
Building a good and fun game with GitHub Copilot (or any AI coding tool) can be deceivingly time-consuming. Even fun vibe-coding projects can get out of hand: the prompt that worked in five minutes pulls you into a polish loop that stretches across two evenings. That is fine, and often the point. Letting yourself get pulled in is one of the fastest ways to learn how the tool actually behaves under sustained use. Just go in with your eyes open.

## Pick a Form, Pick a Hook
The two ingredients are a form (a game the model knows) and a hook (something you actually care about). A random prompt produces a random result. A specific one produces a small thing that feels like yours.

**Forms that one-shot well with GitHub Copilot:**

* **Flappy Bird.** A bird, gravity, two pipes, a score. Trivial physics, instantly playable.
* **Wordle.** Five letters, six guesses, green/yellow/grey. A custom word list takes thirty seconds.
* **Snake or Tetris.** Classic arcade. The model gets the controls right.
* **Top-down RPG.** A character, walls, NPCs you bump into for a line of dialogue. Slow to perfect, fun to start.
* **Trivia or Jeopardy.** A board of categories and questions. Plug in real content from a doc you have lying around.

**Hooks that turn the form into something memorable:**

* A coworker’s birthday, an anniversary, a farewell.
* A topic you are studying right now: a language, a subject, a book.
* Documents you have lying around: technical documentation, project specifications, the last slide deck you presented.
* Contents of our VIB website.

Combine them. “Wordle where every word is a meeting type at our company.” “Flappy Bird themed around my coworker's birthday (include some personalized elements).” “A two-room top-down RPG to guide customers through the VIB core facilities.” The combination is what makes the result specific. The combination is also what makes it fun to share afterwards, which is what gets you to do it again.

---

## Instructions

### Step 1: Set Up the Project
1. Create an empty folder and open it in VS Code. `mkdir ~/projects/first-game && cd ~/projects/first-game && code .`
2. Open your new workspace and open the **GitHub Copilot Chat** panel.
3. *(Optional) Open the workspace in a Dev Container to ensure a clean environment. See the previous exercise for instructions on how to do this.*

### Step 2: Pick a Form and a Hook
1. Pick a form and a hook in under a minute. Do not agonise. The first idea that makes you smirk is the right one. 
2. Write one sentence: “A <form> themed around <hook>.”

*Examples:*
* “A Wordle clone where every word is a meeting type at our company.”
* “Flappy Bird where the bird is our CEO’s coffee mug and the pipes are calendar invites.”
* “A top-down RPG of my apartment where my cat is the final boss.”

### Step 3: Prompt GitHub Copilot
1. Hand the sentence to GitHub Copilot. 
2. Add: “Single HTML file, no build step, opens in a browser.” That keeps the result trivial to run.
   * *Example prompt:* `Build a Wordle clone where every word is a meeting type at our company. Single HTML file, no build step, opens in a browser.`
3. Let it run. Don’t interrupt. Don’t course-correct. Just watch what shows up.

### Step 4: Play and Evaluate
1. Open the result. Most likely, you will open `index.html`. 
2. Play it for one minute. 
3. Notice the parts that surprised you (the model picked a palette you didn’t ask for) and the parts that fell flat.

### Step 5: Make It Better
1. Tell the agent “make it better.” Twice. No other instructions. 
2. Read the diff each round. Notice what it tightens (layout, palette, edge cases) and what it leaves alone. Round three almost always feels crafted in a way round one didn’t.

### Step 6: Share It
1. Send it to one person. A teammate, a friend, a group chat. 
2. Their reaction is the feedback that matters, and the reaction is what tends to make you want to keep building, which is the whole point of the exercise.

---

## Reflection
1. **Was the version Copilot built on round zero already playable, or did the make-it-better passes do most of the work?** What does that tell you about how to point the tool tomorrow on something that matters?
2. **Pick one thing at your work that is currently a slide deck, a doc, or a meeting.** Could that thing be a game? If yes, the prompt for your next vibe-coding session is already written.

01
Create an empty folder and open it in VS Code. `mkdir ~/projects/first-game && cd ~/projects/first-game && code .`, then open GitHub Copilot Chat (or use Copilot Edits).

02
Pick a form and a hook in under a minute. Do not agonise. The first idea that makes you smirk is the right one. Write one sentence: “A <form> themed around <hook>.”

Examples:

“A Wordle clone where every word is a meeting type at our company.”
“Flappy Bird where the bird is our CEO’s coffee mug and the pipes are calendar invites.”
“A top-down RPG of my apartment where my cat is the final boss.”
03
Hand the sentence to GitHub Copilot. Add: “Single HTML file, no build step, opens in a browser.” That keeps the result trivial to run.

Build a Wordle clone where every word is a meeting type at our company. Single HTML file, no build step, opens in a browser.
Let it run. Don’t interrupt. Don’t course-correct. Just watch what shows up.

04
Open the result. Most likely: open index.html. Play it for one minute. Notice the parts that surprised you (the model picked a palette you didn’t ask for) and the parts that fell flat.

05
Tell the agent “make it better.” Twice. No other instructions. Read the diff each round. Notice what it tightens (layout, palette, edge cases) and what it leaves alone. Round three almost always feels crafted in a way round one didn’t.

06
Send it to one person. A teammate, a friend, a group chat. Their reaction is the feedback that matters, and the reaction is what tends to make you want to keep building, which is the whole point of the exercise.

Reflect
Was the version Copilot built on round zero already playable, or did the make-it-better passes do most of the work? What does that tell you about how to point the tool tomorrow on something that matters?
Pick one thing at your work that is currently a slide deck, a doc, or a meeting. Could that thing be a game? If yes, the prompt for your next vibe-coding session is already written.