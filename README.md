# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

The purpose of the game is to have the User guess a number within a range. Hints can be given if they're close or not. The game ends when the User guesses the number correctly. 
- [x] Detail which bugs you found.

I found a wide range of bugs, all logic and or display issues. Values don't update or display correctly on the backend or frontend. The "New Game" button wouldn't truly reset the game. The attempts would reset but not the history, making it impossible to enter guesses. 
- [x] Explain what fixes you applied.

The ones I fixed were the hint messages and the New Game functionality as I saw those important to have as an MVP to then build off with the other functions. For the hint messages, the conditional logic was fine but the messages being displayed were incorrect. So I updated those and for the New Game button, there were variables that failed to be reset BEFORE the app was 'rerun'. So I added resets for score, status, and history. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess into the text field.
2. User enters 84.
3. Game returns a message as a hint: "Go LOWER!"
4. User enters 24.
3. Game returns a message as a hint: "Go HIGHER!"
4. Continue until the User guesses correctly.
5. Game ends and a User can click on "New Game" to start again with a fresh secret number.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
