"""
Main module for the game
"""

# Import necessary modules
import random  # For generating random words from different categories
import string  # For accessing all uppercase letters in the alphabet
import sys  # For system-specific functionality like exiting the game

# Word banks imported
# Defined categories for word selection
from natural_phenomena import WORD_BANK_ONE
from months_seasons import WORD_BANK_TWO
from animals import WORD_BANK_THREE

from hangman import (
    little_man_pic,
    little_man_one,
    little_man_two,
    little_man_three,
    little_man_four,
    little_man_five,
    little_man_six,
    little_man_seven
)


def introduction():
    """
    Displays an introduction to the Italian Hangman game.

    Provides an introductory rhyme and instructions
    for playing the game.
    """
    print("")
    print("\n  WELCOME TO THE ITALIAN HANGMAN GAME\n")
    # Display introductory rhyme
    print("  In Italy we play a wordy game so grand,")
    print("  It is the Hangman game! Where letters in the air stand.")
    print("\n  Try guessing the hidden word, letter by letter,")
    print("  for the poor man's fate - you'll make it so much better.")
    print("\n  The keyboard is right there - be ready to play.")
    print("  Try your best - don't let the hangman swing today.")
    print("\n  From 'A' to 'Z', choose your letters with care,")
    print("  and remember: in Italian we don't use y or j or x.")
    print("\n  So guess away - don't let your chances slip,")
    print("  as the Italian Hangman, it's a challenging trip.")
    print("\n  Guess the word, solve the puzzle, and win the day!")
    print("  Or watch the hangman's noose, in the breeze, sway.\n")
    print("  ________________________________\n")  # Visual separation
    print("  You have seven attempts to guess the Italian word.")


def get_random_word():
    """
    Allows the player to choose a category and selects
    a random word from that category's WORD BANK.

    Returns:
        str: Randomly selected word from the chosen
        category's WORD BANK.
    """
    # Categories available for word selection
    categories = {1: "Natural phenomena", 2: "Months & Seasons", 3: "Animals"}
    # Display category options
    print(
        "\n  Select a category: \n\n  1: Natural phenomena\n  "
        "2: Months & Seasons\n  3: Animals\n"
    )

    while True:
        selection = input("  Please indicate"
                          " the category's number: \n  ").strip()

        if selection in ["1", "2", "3"]:
            category_number = int(selection)
            selected_word_bank = None

            # Determine the selected category and its associated WORD BANK
            if category_number == 1:
                selected_word_bank = WORD_BANK_ONE
                print("\n  Categoria: Fenomeni naturali")

            elif category_number == 2:
                selected_word_bank = WORD_BANK_TWO
                print("\n  Categoria: Mesi & stagioni")

            elif category_number == 3:
                selected_word_bank = WORD_BANK_THREE
                print("\n  Categoria: Animali")
            # If a WORD BANK is selected, choose a random word
            # from it and return it in uppercase
            if selected_word_bank:
                random_word = random.choice(selected_word_bank)
                return random_word.upper()
        else:
            print("  Invalid choice."
                  " Please select a valid category. [1, 2, 3]")


def display_hangman(num_attempts):
    """
    Display the hangman's image based on the number of attempts left.

    Args:
    num_attempts (int): Number of attempts remaining
    before the hangman is fully drawn.

    Returns:
    None: Prints the corresponding hangman's image
    based on the number of attempts left.
    """
    if num_attempts == 6:
        # Display the hangman's image with one stage drawn
        little_man_one()
    elif num_attempts == 5:
        # Display the hangman's image with two stages drawn
        little_man_two()
    elif num_attempts == 4:
        # Display the hangman's image with three stages drawn
        little_man_three()
    elif num_attempts == 3:
        # Display the hangman's image with four stages drawn
        little_man_four()
    elif num_attempts == 2:
        # Display the hangman's image with five stages drawn
        little_man_five()
    elif num_attempts == 1:
        # Display the hangman's image with six stages drawn
        little_man_six()
    else:
        # Display the hangman's complete image
        little_man_seven()


def print_dashed_word(word, num_attempts):
    """
    For a given word, prints the letters guessed correctly
    or dashes for unguessed letters. Reduces the number of
    attempts for incorrectly guessed letters and displays
    part of the hangman's picture.

    Args:
    word (str): The word to be guessed by the player.
    num_attempts (int): The number of attempts allowed
    before the game ends.

    Returns:
    tuple: A tuple containing the updated word list and
    the remaining attempts.

    Explanation:
    The function initializes the word list with dashes
    representing unguessed letters.
    It prompts the player for a letter and handles the guess
    accordingly:
        - If the letter is correct, it reveals the letter
          in the word.
        - If the letter is incorrect, it reduces the attempts
          and displays part of the hangman image.
        - If the attempts run out, the player loses,
          revealing the word and clearing the used letters.
    """
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Guessed letters by the player
    # Initialize word list with dashes
    word_list = ["_"] * len(word)

    while "_" in word_list and num_attempts > 0:
        # Display the current word (e.g., G _ _ T O)
        print("\n  Word: ", " ".join(word_list))
        # Letter guessed by player
        player_letter = input(
            "\n  Guess a letter: \n  "
        ).upper().strip()
        print("  ________________________________\n")  # Visual separation

        if (
            player_letter in alphabet - used_letters
        ):  # Letter guessed by player
            used_letters.add(
                player_letter
            )  # Add the guessed letter to used_letters
            if (
                player_letter in word_letters
            ):  # Check if the guessed letter is in the word
                word_letters.remove(
                    player_letter
                )  # Remove correctly guessed letter from word_letters
                print("\n  Well done! Correct letter.")
            elif player_letter not in word_letters:
                print("\n  The letter is not in the word!\n")
                num_attempts -= 1  # Decrease the number of attempts by 1
                display_hangman(
                    num_attempts
                )  # Display the hangman image based on attempts
                if num_attempts == 0:  # If attempts run out, the player loses
                    print("\n  YOU LOST!")
                    print("  The Italian word was:", word)
                    used_letters.clear()  # Clear used_letters
                    return word_list, num_attempts
            # Update the word list to reveal correctly guessed letters
            for i, letter in enumerate(
                word
            ):
                if (
                    letter == player_letter
                ):
                    word_list[
                        i
                    ] = player_letter  # Index is updating with letter
            print("  Attempts left: ", num_attempts)
            print("  Letters used: ", ", ".join(used_letters))
        elif player_letter in used_letters:  # If the letter is already guessed
            print("  You have already used this letter. Guess again.")
        else:  # If an invalid character is entered
            print("  Invalid character. Try again.")
    # Display the final word with guessed letters
    print("\n  Word: ", " ".join(word_list))
    return word_list, num_attempts


def restart_game(current_word):
    """
    Allows the player to restart the game upon winning or losing.

    Args:
    current_word (str): The current word being played by the player.

    Returns:
    tuple: A tuple containing the number of attempts and a new randomly
    selected word.

    Explanation:
    The function prompts the player if they want to restart the game.
    - If the player chooses 'yes', the function resets the number of
      attempts to 7 and selects a new word.
    - If the player chooses 'no', the game exits.
    """
    print("\n  WOULD YOU LIKE TO PLAY AGAIN?")

    while True:
        answer = input("  [Yes/No]: \n  ").strip().lower()
        if answer == "yes":
            print(
                "\n  Have another go! \n "
                " Guess the Italian word and save the little man."
            )
            num_attempts = 7
            new_word = get_random_word()  # Get a new random word
            return num_attempts, new_word  # Return values to the main function
        elif answer == "no":
            print("  Okay. Bye bye!")
            sys.exit()  # Exit the game if the player chooses not to restart
        else:
            print("  Please enter 'Yes' or 'No'")


def ask_to_play():
    """
    Asks the player if they want to start the game.

    Returns:
    None

    Explanation:
    The function prompts the player to start the game
    by entering 'yes' or 'no'.
    - If 'yes', the game starts.
    - If 'no', the game exits.
    - If the player enters anything other than 'yes' or 'no',
      it asks for a correct input.
    """
    while True:
        answer = (
            input("  WOULD YOU LIKE TO PLAY? [Yes/No]\n  ")
            .strip()
            .lower()
            )

        if answer == "yes":
            print("\n  Let's play!"
                  " Guess the Italian word and defeat the hangman.")
            break  # Exit the loop as the user wants to play
        elif answer == "no":
            print("  Okay. Ciao!")
            sys.exit()  # Exit the game
        else:
            print("  Please enter 'Yes' or 'No'")


def main():
    """
    Starts and controls the game dynamics.

    Returns:
    None

    Explanation:
    The main function controls the flow of the game by:
    - Displaying an introduction to the game.
    - Asking the player if they want to play.
    - Obtaining a random word from the word banks.
    - Entering a game loop and checking for victory conditions.
    """
    num_attempts = 7

    # Introduction to the game
    print()
    little_man_pic()
    introduction()
    ask_to_play()

    # Get random word from word banks
    word = (
        get_random_word()
    )  # Random word from the word banks stored in the variable called word
    print("")

    # Game loop & victory condition
    while True:
        # Obtain the current status of the word and remaining attempts
        current_word, num_attempts = print_dashed_word(word, num_attempts)

        # Check for victory condition: word guessed correctly
        if (
            num_attempts != 0 and "".join(current_word) == word
        ):  # Compare the joined character with original word
            print("")
            print("  CONGRATULAZIONI!"
                  " You have defeated the Italian hangman!\n")
            # Restart the game if the player wins
            num_attempts, word = restart_game(
                current_word
            )  # Unpack tuple in two variables
            continue  # Continue the game loop
        # Check for losing condition: no attempts left
        elif num_attempts == 0:
            num_attempts, word = restart_game(current_word)
            continue  # Continue the game loop


main()
