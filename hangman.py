"""
=====================================================
 Project      : Hangman Game (Text-Based)
 Course       : Python Programming - 1st Year CSE
 Description  : A simple command-line Hangman game
                where the player guesses letters to
                find a hidden word within 6 wrong tries.
=====================================================
"""

# 'random' is a built-in Python module.
# We use it to randomly pick a word from our word list.
import random


# ---------------------------------------------------
# Function 1: choose_word()
# Purpose: Randomly select one word from a fixed list.
# ---------------------------------------------------
def choose_word():
    # This is our predefined list of exactly 5 words.
    word_list = ["python", "computer", "college", "student", "hangman"]

    # random.choice() picks one random item from the list.
    selected_word = random.choice(word_list)

    return selected_word


# ---------------------------------------------------
# Function 2: display_word()
# Purpose: Show the word with guessed letters revealed
#          and unguessed letters as underscores (_).
# ---------------------------------------------------
def display_word(word, guessed_letters):
    # We build the display string letter by letter.
    display = ""

    for letter in word:
        if letter in guessed_letters:
            # If the letter has been guessed, show it.
            display = display + letter + " "
        else:
            # Otherwise, hide it with an underscore.
            display = display + "_ "

    # .strip() removes the extra trailing space at the end.
    return display.strip()


# ---------------------------------------------------
# Function 3: get_guess()
# Purpose: Take input from the player and validate it.
#          Keeps asking until a valid, new letter is given.
# ---------------------------------------------------
def get_guess(guessed_letters):
    while True:
        # input() takes text from the user.
        # .lower() converts it to lowercase so that
        # "A" and "a" are treated the same way.
        # .strip() removes accidental spaces.
        guess = input("Enter a letter: ").lower().strip()

        # Case 1: Empty input (user just pressed Enter)
        if len(guess) == 0:
            print("Invalid input! You cannot enter nothing. Try again.")

        # Case 2: More than one character entered
        elif len(guess) > 1:
            print("Invalid input! Please enter only ONE letter at a time.")

        # Case 3: Input is not an alphabet letter (number/symbol)
        elif not guess.isalpha():
            print("Invalid input! Please enter an alphabet letter only (a-z).")

        # Case 4: Letter already guessed before (duplicate)
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")

        # If none of the above problems occurred, the guess is valid.
        else:
            return guess


# ---------------------------------------------------
# Function 4: play_game()
# Purpose: Main function that runs the entire game
#          using a while loop until win or lose.
# ---------------------------------------------------
def play_game():
    print("=" * 50)
    print(" Welcome to HANGMAN - Guess the Word! ")
    print("=" * 50)

    # Step 1: Choose a random word for this round.
    word = choose_word()

    # This list stores every letter the player has guessed
    # (both correct and wrong), used to avoid duplicates.
    guessed_letters = []

    # This list stores only the WRONG guessed letters.
    wrong_letters = []

    # Maximum number of incorrect guesses allowed.
    max_attempts = 6

    # Tracks how many wrong guesses have been made so far.
    wrong_attempts = 0

    # The main game loop.
    # It keeps running as long as the player has attempts left
    # AND the word is not fully guessed yet.
    while wrong_attempts < max_attempts:

        # Display the current state of the word.
        print("\nWord: " + display_word(word, guessed_letters))

        # Show correctly guessed letters so far.
        correct_so_far = [letter for letter in guessed_letters if letter not in wrong_letters]
        print("Correct guesses:", correct_so_far)

        # Show wrong guessed letters so far.
        print("Wrong guesses:", wrong_letters)

        # Show remaining attempts left.
        print("Remaining attempts:", max_attempts - wrong_attempts)

        # Ask the player for a valid letter guess.
        guess = get_guess(guessed_letters)

        # Add this new guess to our guessed_letters list.
        guessed_letters.append(guess)

        # Check whether the guessed letter is in the word.
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_letters.append(guess)
            wrong_attempts = wrong_attempts + 1

        # Check win condition:
        # If every letter of the word is inside guessed_letters,
        # the player has found the complete word.
        word_completed = True
        for letter in word:
            if letter not in guessed_letters:
                word_completed = False
                break

        if word_completed:
            print("\n" + "=" * 50)
            print("Word:", display_word(word, guessed_letters))
            print(f"CONGRATULATIONS! You guessed the word '{word}' correctly!")
            print("=" * 50)
            return  # Ends the game immediately (win case)

    # If the while loop ends because wrong_attempts reached max_attempts,
    # it means the player has lost the game.
    print("\n" + "=" * 50)
    print("You have run out of attempts. GAME OVER!")
    print(f"The correct word was: '{word}'")
    print("=" * 50)


# ---------------------------------------------------
# Program entry point.
# This ensures play_game() runs only when this file
# is executed directly (not when imported elsewhere).
# ---------------------------------------------------
if __name__ == "__main__":
    play_game()
