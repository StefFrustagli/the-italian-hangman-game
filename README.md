# THE ITALIAN HANGMAN GAME

*It's time to play the **Italian hangman game**!*
This is a Python terminal game that runs on Heroku's mock terminal created by the Code Institute.

This game is intended for intermediate Italian learners and Italians speakers (children or adults) who enjoy simple word guessing games. As the instructions are given in English, a basic understanding of English is also required. It is a classic version of the game in which the player must guess the word letter by letter within a certain number of attempts.

## Table of Contents

- [User Experience (UX)](#user-experience)
- [Features & Game functionalities](#features-and-game-functionalities)
- [Tecnologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience

### Project's goal & Design 

The idea was to make a simple and essential game that had a retro appeal. I wanted to limit possible aesthetic improvements and let the player experience the pure joy or frustration of guessing words. The game mechanics were designed to be straightforward and immediate. As a result, the game is fast and can be enjoyed during a study or work break.

### Ideal players

- Learner of Italian as a second language who wish to practice their Italian words.
- Casual Italian speaker player with a basic knowledge of English who wants to play a guessing word game.
- Casual player with a basic knowledge of Italian and English who wants to distract themselves from daily tasks.
- Gamer who loves word retro games.
  
### User stories

#### Italian learner:
- I want to play a word game to practice my Italian.
- I want to test my Italian knowledge and see how many words I know. 
- By guessing Italian words, I want to increase my Italian vocabulary.
   - I am more likely to memorize words in another language by playing an interactive game.
- For the guessing choice to be limited, I would like to have the option to choose from different categories.
- I want to play a straight-forward word game.

#### Italian speaker player:
- I want to spend a few minutes distracting myself from routine tasks.
- I want to play an online game that doesn't take a lot of time.
- I want to have fun guessing a few words in my own language.
- I want to play a game with my children.
- I want my children to play a game to practise/learn Italian words.
- I want to play a retro/nostalgic game that I used to play in my childhood.
- I want to play a straight-forward word game.

#### Casual player (Italian as a second language):
- I want to have fun and check the Italian words I know/remember.
- I want to spend a few minutes distracting myself from routine tasks.
- I want to play a retro/nostalgic game that I used to play in my childhood.
- I want to play a straight-forward word game.

#### Retro game lover
- I want to play a simple, quick word game that doesn't indulge in fancy aesthetics. 
- I want to feel like I'm in the 80s.
- I want to play a straight-forward word game that can be played in a terminal.

#### What the user might expect:
- To understand the game's rules easily.
- A simple game dynamic.
- A fast and interactive game.
- Categories of words to select.
- To see the 

#### As a developer, I expect:
- To provide an easy and logical navigation within the game.
- To make the game as clear and simple to play as possible.
- To provide clear instructions.
- To provide some fun with a chance game.
- To show my JavaScript skills.

## Aspects of planning
### Flowchart
I created this flowchart when I was planning the logic for the game. Even though it is rough and does not contain all the passages, it has helped me develop the game dynamic.

FLOWCHART

### Game flow

Before realizing the project, I took the following notes:
1. User opens terminal. Welcome message appears with nursery rhymes to explain the game.
2. The user is asked if they want to play.
   - If 'yes', the game starts.
   - If 'no', the game exits.
3. If user wants to play, the game displays a random dashed version of the word (example: _ _ _ _ )
 - Dashes are displayed instead of letters (user knows the word length).
 - When the correct letter is guessed, it replaces the dash.
 - Information given to the player:
   - Word: _ _ _ _ _ _ 
   - Length of the word
   - Letters guessed: a, b
   - Attempts left: num
4. User asked to choose a letter.
5. A message appears: 
   - if the letter is incorrect: "Letter wrong. Please try again."
      - A part of the hangman picture is shown. 
   - if the letter is correct: "Well done"
6. User is asked to input another letter. 
   - It will be added at the bottom of the info provided.
   - This will happen seven times, depending on how many attempts the player has.
   - When the picture is complete, the player loses the game.
   - It will be displayed in the correct position if the letter is correct.
   - Until the user completes the word or the attempts are over, the user will be asked to guess again.
7. If the player loses or wins, a message will ask if they wish to play again.
8 - User is asked if the want to play again. Return to point 3.

## Features and game functionalities

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