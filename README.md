# THE ITALIAN HANGMAN GAME

*It's time to play the **Italian hangman game**!*
This is a Python terminal game that runs on Heroku's mock terminal created by the Code Institute.

This game is intended for intermediate Italian learners and for native Italian children who are learning to read and write or native adults. As the instructions are given in English, a basic understanding of English is also required.

## How to play
The goal of the game is to identify the words correctly in order to save the little man from execution. There are seven possible attempts. To simplify guessing, I have identified 3 different categories that the player can select at the beginning of the game.



# Introductory nursery rhyme 

*In Italy we play a wordy game so grand,* <br>
*It is the Hangman game! Where letters in the air stand.* <br>

*Trying guessing the hidden word, letter by letter,* <br> 
*and the poor man's fate - you'll make it so much better.* <br> 

*The keyboard is right there - be ready to play.* <br>
*Try your best - don't let the hangman swing today.* <br>
*From "A" to "Z," choose your letters with care,* <br>
*and remember: in Italian we don't use y or j or x.* <br>

*So guess away - don't let your chances slip,* <br>
*as the Italian Hangman, it's a challenging trip.* <br>
*Guess the word, solve the puzzle, and win the day!* <br>
*Or watch the hangman's noose, in the breeze, sway.*<br> 

## Flowchart

add flow chart here

## Game Dynamic 
Here are some notes I took before realising the project:

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