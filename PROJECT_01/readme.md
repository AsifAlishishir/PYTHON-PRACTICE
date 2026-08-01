# 🐍 Snake, Water, Gun Game

A simple command-line game in Python — a Rock-Paper-Scissors style game where you play against the computer.

## How It Works

- **Snake** beats **Water**
- **Water** beats **Gun**
- **Gun** beats **Snake**

Each choice is mapped to a number (`Snake = 1`, `Water = 0`, `Gun = -1`), and the winner is decided by comparing the player's and computer's choices.

## Tech Used

- Python 3
- Built-in `random` module (for computer's choice)

## Key Features

- Random computer opponent using `random.choice()`
- Dictionary-based mapping for clean choice comparison instead of long if-else chains
- Input validation — invalid inputs (anything other than `s`, `w`, `g`) are rejected and the user is re-prompted, so the program never crashes on bad input

## How to Run

```bash
python project.py
```

Then enter your choice when prompted:
```
Enter your choice [S]nake / [W]ater / [G]un:
```

## What I Practiced

- Working with dictionaries for lookup-based logic instead of repetitive conditionals
- Input validation using a `while` loop
- Basic game-state logic (win / lose / draw conditions)