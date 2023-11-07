# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


"""
1. User opens terminal. Welcome message appears with nursery rhyme to explain the game.
2. User asked if they want to play. 
  2B If 'yes', the game starts. 
  2C If 'no', the game exits.
3. If 2.B, the game starts displaying a random dashed version of the word -- 
   dashes are displayed instead of letters (user knows the length of the word). 
   When correct letter is guessed, it will replace the dash.
  3A Info given to the player:
      - Word: _ _ _ _ _
      - Length: num
      - Letters guessed: a, b 
      - Attempts left: num
4. User asked to choose a letter.
5. 5A If letter is wrong, a message appears: "Letter wromg. Try again." Input to choose another letter.
      A part of the hangman picture is shown. It is added at the bottom of the info provided above. 
      This will happen for seven times, the attempts the player has. When the picture is complete, the player loses the game
   5B If the letter is right, the letter will be displayed in the correct position. 
      The user will be asked to guess again till the attempts end or the word is completed.


"""
# Import random module to choose a random word from lists of words
import random

# Category: natural phenomena
WORD_BANK_ONE = "temporale, pioggia, grandine, vento, arcobaleno, fulmine, tempesta, tuono, maremoto, terremoto, alluvione, frana, valanga, tornado".split(',')

# Category: months & seasons
WORD_BANK_TWO = "gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre, primavera, estate, autunno, inverno".split(',')

# Category: animals
WORD_BANK_THREE = "cammello, rinoceronte, elefante, ermellino, bisonte, canguro, lucertola, coccodrillo, anaconda, criceto, cavallo, pantera, delfino, balena, gorilla, antilope, asino, murena, aquila, rondine".split(',')

# Number of attempts
NUM_ATTEMPTS = 7

def little_man_pic():
        print("  +---+")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("     ===")        


def little_man_one():
        print("       ")
        print("       ")
        print("       ")
        print("       ")
        print("     ===")  
def little_man_two():
        print("        ")
        print("        ")
        print("        ")
        print("      |")
        print("     ===")  

def little_man_three():
        print("        ")
        print("        ")
        print("      |")
        print("      |")
        print("     ===")  

def little_man_four():
        print("        ")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")  

def little_man_five():
        print("    --+")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")  

def little_man_six():
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")  

def little_man_seven():
        print("  +---+")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("     ===")  


def introduction():
    """
    Introduction to the game with a nursery rhyme
    """
    print("\nWELCOME TO THE ITALIAN HANGMAN GAME\n")
    print("In Italy we play a wordy game so grand,")
    print("It is the Hangman game! Where letters in the air stand.")
    print("\nTry guessing the hidden word, letter by letter,")
    print("for the poor man's fate - you'll make it so much better.")
    print("\nThe keyboard is right there - be ready to play.")
    print("Try your best - don't let the hangman swing today.")
    print("\nFrom 'A' to 'Z', choose your letters with care,")
    print("and remember: in Italian we don't use y or j or x.")
    print("\nSo guess away - don't let your chances slip,")
    print("as the Italian Hangman, it's a challenging trip.")
    print("\nGuess the word, solve the puzzle, and win the day!")
    print("Or watch the hangman's noose, in the breeze, sway.\n")
    print("\nWOULD YOU LIKE TO PLAY? \n")
    print(input("Yes/No: "))

def restart_game():
    """
    If player wins or loses, ask if they want to restart the game
    """
    print("\nWOULD YOU LIKE TO PLAY AGAIN? \n")
    print(input("Yes/No: "))
        


def select_cathegory():
       """
       select word bank and from there generate a random word
       """

def get_random_word():
       """ 
       Get a random word from the bank word and return it.
       When user starts the game, a random word is generated.
       """

def print_dashed_word():
       """
       Given a word, print the letters that have been guessed. Otherwise, print dashes.

       e.g. for the word 'gatto', if 'g' and 'a' have been guessed, print 'g a _ _ o'
 
       word: str - the word to print out
       guessed_letters: list of str - a list of letters in word that have already been guessed
    
       """

       blanks = '_' * len(secretWord) # Repeat underscoring as many times as the word length


# Main function       
def main():
       """
       Activate the game dynamic:
       """
       little_man_pic() 
       introduction()
       """
       word = get_random_word()
       correctly_guessed_letters = []

       print_dashed_word(word, correctly_guessed_letters)

       for i in range(NUM_ATTEMPTS):
       """
main()