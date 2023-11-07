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