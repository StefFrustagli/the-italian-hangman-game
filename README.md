# THE ITALIAN HANGMAN GAME

*It's time to play the **Italian hangman game**!*
This is a Python terminal game that runs on Heroku's mock terminal created by the Code Institute.

This game is intended for intermediate Italian learners and Italians speakers (children or adults) who enjoy simple word guessing games. As the instructions are given in English, a basic understanding of English is also required. It is a classic game in which the player must guess the word letter by letter within seven attempts.






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

## Table of Contents

- [User Experience (UX)](#user-experience)
- [Features](#features)
- [Tecnologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience

### Project's goal & Design 

The idea was to make a simple and essential game that had a retro appeal. The idea was to limit possible aesthetic improvements and let the player experience the pure joy or frustration of guessing words. The game mechanics were designed to be straightforward and immediate. As a result, the game is fast and can be enjoyed during a study or work break.


### Ideal player

- Learners of Italian as a second language who wish to practice their Italian words.
- Someone with a basic knowledge of Italian and English who wants to play a guessing word game.
- Someone who wants to distract themselves from daily tasks by guessing a word.
- Gamer who loves word retro games.
  
### User stories

#### Italian learners:
- I want to see an example of a JavaScript game in action.
- I want to try the classic 'Rock Paper Scissors' game created with basic JavaScript knowledge.
- I want to look at a game and see if I'm able to understand how it works and build a similar version.

#### Rock, paper, scissors game enthusiasts:
- I want to play a classic version of the Rock, paper and scissors game.
- I like the idea of competing against a robot.
- I like the game design and want to try this version of the game.

#### Casual players:
- I want to spend a few minutes distracting yourself from routine tasks.
- I want to play an online game that doesn't require too much concentration.
- I want to play an online game against a chance-dominated computer and test my luck.

#### What the user might expect:
- To understand the game's rules easily.
- To see the score counters.
- To see hands with both choices.

#### As a developer, I expect:
- To provide an easy and logical navigation within the game.
- To make the game as clear and simple to play as possible.
- To provide clear instructions.
- To provide some fun with a chance game.
- To show my JavaScript skills.


## Features & Game functionalities

## How to play
The goal of the game is to identify the words correctly in order to save the little man from execution. There are seven possible attempts. To simplify guessing, I have identified 3 different categories that the player can select at the beginning of the game.

### Existing Features

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


### Future features and general aspects left to implement
- Increase the number of words in the bank.
- Provide more categories to choose from. 
- Add a tracking score to Keep track of players' progress.


## Technologies used
### Languages

- The only program language used in this project is **Python3**

### Frameworks, Programs & Libraries

- [GitHub Pages:](https://pages.github.com/) is where the site is hosted.
- [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/) was used as the repository for the project after being pushed from Git.
- [Codeanywhere](https://codeanywhere.com/) was used as online IDE.
- [Figma:](https://www.figma.com/) was used to create wireframes during the design process.
- [Google Fonts:](https://fonts.google.com/) was used to import fonts into the style.css.
- [Font Awesome:](https://fontawesome.com/) was used to add icons in the footer.
- [ImgBB:](https://imgbb.com/) was used to upload images and extract the source code.
- [Am I Responsive?](http://ami.responsivedesign.is) was used to generate the mockup of the website.
- [Table Convert](https://tableconvert.com/) was used to generate tables for the TESTING.md file.


## Testing

Testing information can be found in [TESTING.md file](TESTING.md).

## Deployment

## Credits

### Content


### Code

As this was my first time building a game with 

### Acknowledgment

For their support, suggestions and feedback, I am very grateful to my mentor Brian Macharia and my fellow classmates on Slack, in particular I want to thank Niclas for his precious support.