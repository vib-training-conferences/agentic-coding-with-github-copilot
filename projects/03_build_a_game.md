# Mini-project: Build a Game

Now that you have a good feel for how Github Copilot works, it is time to build something with it. The first thing you build with a new tool should be small, fun, and disposable, because that is how you learn what the tool can actually do without your stakes clouding the lesson. In this exercise, you will build a game with GitHub Copilot in a single HTML file. 

The advantage of building a simple game is that it is a self-contained project with an instant feedback loop. You can see the results immediately, and you can iterate quickly without worrying about breaking anything important. Plus, it’s fun!

## Choosing a Game
The game you choose should be something simple that can be implemented in a single HTML file. Some popular choices include: Flappy Bird, Wordle, Snake, Tetris, or a simple top-down RPG. The key is to pick something that you find interesting and that you think will be fun to play.

You can also add a personal touch to the game by choosing a theme or a hook that is relevant to you. For example, you could create a Flappy Bird clone where the bird is your favorite animal, or a Wordle game where the words are related to a project you are working on. The more specific and personal the hook, the more fun it will be to play and share with others.

## Warning
Building a good and fun game with GitHub Copilot (or any AI coding tool) can be deceivingly time-consuming. Even fun vibe-coding projects can get out of hand: the prompt that worked in five minutes pulls you into a polish loop that stretches across two evenings. That is fine, and often the point. Letting yourself get pulled in is one of the fastest ways to learn how the tool actually behaves under sustained use. Just go in with your eyes open.

---

## Instructions

### Step 1: Set Up the Project
1. Create a new, empty folder for your project and open it in VS Code. This will be your workspace for the game.
2. Open your new workspace and open the **GitHub Copilot Chat** panel.
3. *(Optional) Open the workspace in a Dev Container to ensure a clean environment. See the previous exercise (05_responsible_use/02_devcontainer.md) for instructions on how to do this.*

### Step 2: Pick a Form and a Hook
1. Pick a form and a hook for your game. Do not think too hard about this, the point of the exercise is to get something fun and playable out the door quickly. The first idea that makes you smirk is the right one.
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