# harshini-hangman-game-2026-
# 🎮 Hangman Game – Text-Based Python Project

## 📌 Project Overview
Hangman is a simple text-based word guessing game developed using Python. The player must guess a randomly selected hidden word by entering one letter at a time.

The player is allowed a maximum of **6 incorrect attempts** to guess the complete word. The game ends when the player correctly guesses the word or runs out of attempts.

## 🎯 Objectives
- To develop a simple interactive game using Python.
- To understand functions and loops.
- To implement random word selection.
- To practice conditional statements and list operations.
- To perform input validation.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Module:** Random (Built-in Python Module)
- **Platform:** Command-Line Interface (CLI)

## ✨ Features
1. **Random Word Selection:** Selects a random word from a predefined list of five words.
2. **Hidden Word Display:** Displays unguessed letters as underscores (_).
3. **Letter Guessing:** Allows players to guess one letter at a time.
4. **Input Validation:** Prevents empty input, numbers, symbols, multiple characters, and repeated guesses.
5. **Attempt Tracking:** Allows a maximum of six incorrect guesses.
6. **Win/Lose Detection:** Displays the result based on the player's performance.

## 📂 Word List
The game randomly selects one word from the following:

- Python
- Computer
- College
- Student
- Hangman

## ⚙️ Functions Used

| Function | Purpose |
|---|---|
| `choose_word()` | Selects a random word. |
| `display_word()` | Displays guessed letters and underscores. |
| `get_guess()` | Accepts and validates user input. |
| `play_game()` | Controls the complete game. |

## ▶️ How to Run the Project

**Step 1:** Install Python on your computer.

**Step 2:** Save the program as `hangman.py`.

**Step 3:** Open the terminal or command prompt.

**Step 4:** Navigate to the folder containing the Python file.

**Step 5:** Run the following command:

```bash
python hangman.py
```

**Step 6:** Start guessing letters and enjoy the game!

## 🎮 Sample Output

```text
==================================================
 Welcome to HANGMAN - Guess the Word!
==================================================

Word: _ _ _ _ _ _
Correct guesses: []
Wrong guesses: []
Remaining attempts: 6

Enter a letter: p
Good job! 'p' is in the word.

Word: p _ _ _ _ _
Correct guesses: ['p']
Wrong guesses: []
Remaining attempts: 6

Enter a letter: x
Sorry, 'x' is not in the word.

Remaining attempts: 5
```

*Note: The actual word is selected randomly, so the output may vary.*

## 📚 Python Concepts Used
- Functions
- Lists
- While Loop
- For Loop
- If-Else Statements
- Random Module
- User Input (`input()`)
- String Methods (`lower()`, `strip()`, `isalpha()`)
- List Comprehension
- Return Statement

## 🚀 Future Enhancements
- Add different difficulty levels.
- Include more words and categories.
- Add a graphical user interface (GUI).
- Add a score and leaderboard system.
- Provide an option to play again.

## 🏁 Conclusion
The Hangman Game is a beginner-friendly Python project that demonstrates fundamental programming concepts through an interactive word guessing game. It improves logical thinking, problem-solving skills, and understanding of Python functions, loops, and conditional statements.

---

**Project:** Hangman Game (Text-Based)  
**Course:** Python Programming  
**Department:** Computer Science and Engineering  
**Level:** First Year CSE
