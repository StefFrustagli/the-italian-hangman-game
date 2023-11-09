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
5. 5A If letter is wrong, a message appears: "Letter wromg. Try again." 
      Input to choose another letter. A part of the hangman picture is shown. 
      It is added at the bottom of the info provided above. 
      This will happen for seven times, the attempts the player has. 
      When the picture is complete, the player loses the game
   5B If the letter is right, the letter will be displayed in the correct position. 
      The user will be asked to guess again till the attempts end 
      or the word is completed.
6. When player loses or wins, a message asking if they want to play again will appear. 
   Return to point 2.      


"""
# Import random module to choose a random word from lists of words
import random
import string

# Category: natural phenomena
WORD_BANK_ONE = "temporale,pioggia,grandine,vento,arcobaleno,fulmine,tempesta,tuono,maremoto,terremoto,alluvione,frana,valanga,tornado".split(',')

# Category: months & seasons
WORD_BANK_TWO = "gennaio,febbraio,marzo,aprile,maggio,giugno,luglio,agosto,settembre,ottobre,novembre,dicembre,primavera,estate,autunno,inverno".split(',')

# Category: animals
WORD_BANK_THREE = "cammello,rinoceronte,elefante,ermellino,bisonte,canguro,lucertola,coccodrillo,anaconda,criceto,cavallo,pantera,delfino,balena,gorilla,antilope,asino,murena,aquila,rondine".split(',')

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
    

def get_random_word():
       """
       If player selects yes, ask them to select a category. 
       Depending on the category selected, a random word from the WORD BANK is selected.
       """
       categories = {
             1: "Natural phenomena",
             2: "Months & Seasons",
             3: "Animals"
       }
       print("\nSelect a category: \n\n 1: Natural phenomena\n 2: Months & Seasons\n 3: Animals\n")

       category_one = categories[1]
       category_two = categories[2]
       category_two = categories[3]
       
       while True:
             selection = input("Please indicate the category's number: ")

             if selection in ["1", "2", "3"]:
                 
                category_number = int(selection)
                selected_word_bank = None
                 
                if category_number == 1:
                    selected_word_bank = WORD_BANK_ONE
                    print("\nCategoria: Fenomeni naturali")
                    
                elif category_number == 2:
                    selected_word_bank = WORD_BANK_TWO
                    print("\nCategoria: Mesi & stagioni")
                    
                elif category_number == 3:
                    selected_word_bank = WORD_BANK_THREE
                    print("\nAnimali")
                    

                if selected_word_bank:
                     random_word = random.choice(selected_word_bank)
                     
                     return random_word.upper()
                

             else:
                 print("invalid choice. Please select a valid category. [1, 2, 3]")
    

def dashed_word(word):
    """
    Given a word, print the letters that have been guessed. Otherwise, print dashes.
    """
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters user has guessed

    # Getting user input
    word_list = ['_'] * len(word)

    while '_' in word_list:
        # Display the current word (e.g., G _ _ T O)
        print("Word: ", " ".join(word_list))

        player_letter = input("\nGuess a letter: ").upper()
        if player_letter in alphabet - used_letters:
            used_letters.add(player_letter)
            if player_letter in word_letters:
                word_letters.remove(player_letter)
                print("\nWell done!")
                for i, letter in enumerate(word):
                    if letter == player_letter:
                        word_list[i] = player_letter
            print("\nYou have used these letters: ", ", ".join(used_letters))
            print("\nAttempts left:\n")            
        elif player_letter in used_letters:
            print("You have already used this letter. Guess again.")
        else:
            print("Invalid character. Try again.")

    print("Word: ", " ".join(word_list))
    
    return word_list




def ask_to_play():
    """
    Define logic at beginning of the game using a while loop.
    If 'yes', the game starts. If 'no', the game exits. 
    If a different word from 'yes' or 'no' is selected,
    a message asked the user to enter the correct words.
    """
    while True:
        answer = input("\nWOULD YOU LIKE TO PLAY? [Yes/No]\n ").strip().lower()
    
        if answer == "yes":
           print("\nLet's play! Guess the Italian word and defeat the hangman.")
           
           break # Exit the loop as the user wants to play
        elif answer == "no":
           print("Okay. Ciao!")
           # Exit the game
           return # Exit the function
        else:
           print("Please enter 'Yes' or 'No'")
    

def restart_game():
    """
    When player wins or loses, ask if they want to restart the game
    """
    print("\nWOULD YOU LIKE TO PLAY AGAIN? \n")
    print(input("Yes/No: "))
        


# Main function 
def main():
       """
       Activate the game dynamic:
       """
       print()
       little_man_pic() 
       introduction()
       ask_to_play()  

       # Get random word from word banks
       word = get_random_word()
       print("")
       current_word = dashed_word(word)
       print("")

       if ''.join(current_word) == word:
        print("Congratulazioni! You've defeated the Italian hangman!\n")

       """ 
       Function to restart the game
       """
       
       """
       word = get_random_word()
       correctly_guessed_letters = []

       

       for i in range(NUM_ATTEMPTS):
       """

       
main()