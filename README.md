# THE ITALIAN HANGMAN GAME

*It's time to play the **Italian hangman game**!*</br>
</br>
This is a Python terminal game that runs on Heroku's mock terminal created by the Code Institute.

This game is intended for intermediate Italian learners and Italians speakers (children or adults) who enjoy simple word guessing games. As the instructions are given in English, a basic understanding of English is also required. It is a classic version of the game in which the player must guess the word letter by letter within a certain number of attempts.

[View the live project here: ](https://the-italian-hangman-game-c1a71b18c016.herokuapp.com/)

![Responsice Mockup](https://i.ibb.co/qRfJtPR/my-screenshots-2023-11-16-at-20-39-24.png) 

## Table of Contents

- [User Experience (UX)](#user-experience)
- [Features & Game functionalities](#features-and-game-functionalities)
- [Tecnologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience

### Project's goal & Design 

The idea was to make a simple and essential game with a retro appeal. I wanted to limit possible aesthetic improvements and let the player experience the pure joy or frustration of guessing words. The game mechanics were designed to be straightforward and immediate. As a result, the game is fast and can be enjoyed during a study or work break.

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
- I want to play a simple, quick classic game that doesn't indulge in fancy aesthetics. 
- I want to feel like I'm in the 80s.
- I want to play a straight-forward word game that can be played in a terminal.

### What the user might expect:
- To understand the game's rules easily.
- A simple game dynamic.
- A fast and interactive game.
- Word categories to choose from.
- As the game progresses and incorrect words are chosen, to see the classic hangman picture.

### As a developer, I expect:
- To provide an easy and logical game dynamic.
- To make the game as clear and simple to play as possible.
- To provide some fun.

## Aspects of planning
### Flowchart
I created this flowchart when I was planning the logic for the game. Even though it is rough and does not contain all the passages, it has helped me with the development of the game dynamic.

![Draft flowchart](https://i.ibb.co/tbNrtxM/flowchart.png)

### Game flow

During the planning process, I took the following notes:
1. User opens terminal. Welcome message appears with nursery rhymes to explain the game.
2. The user is asked if they want to play:
   - If 'yes', the game starts.
   - If 'no', the game exits.
3. If user wants to play, the game displays a random dashed version of the word (example: _ _ _ _ )
 - Dashes are displayed instead of letters (user knows the word length).
 - When guessed correctly, the correct letter replaces the dash.
 - Display for the player:
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
   - If the player has attempts left, they will be asked to guess again.
7. When the player has zero attempts left, the handman picture is complete and the game is over. Display message: "You lost."
8. If the player guesses all the letters correctly, they win the game. Display message: "You won."  
9. Both loss and win will prompt a message asking if they want to continue playing.

## Features and game functionalities

### How to play
The goal of the game is to identify the word correctly in order to save the little man from execution. There are seven possible attempts. As a way of simplifying the guessing game, I have defined three different categories the player can choose from at the beginning.

### Existing Features

#### Introduction
When the terminal is open, a classic Hangman game picture is displayed.
[PIC]
Afterwards, a message welcoming the player is accompanied by a nursery rhyme that gives a jolly introduction to the game. As an alternative to the usual rules list, I came up with something that tries to grab the user's attention.

[PIC TERMINAL]

After that, the user is given a line of instructions with the number of attempts they have in order to guess the word. This is followed by an invitation to play, in capital letters, to which the user can reply and start the game dynamic.

##### Introductory nursery rhyme 

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

#### User interactions 

TO BE ADDED


### Future features and general aspects left to implement
- Increase the number of words in the word bank.
- Provide more categories to choose from. 
- Add a tracking score to keep track of players' progress.


## Technologies used

- [Python:](https://www.python.org) Hight-level programming language used.
- [PEP8](http://pep8online.com/) was used to check the code for PEP8 requirements.
- [Heroku: Cloud Application Platform](https://dashboard.heroku.com/apps) was used for the deployment.
- [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used as the repository for the project after being pushed from Git.
- [VSCode](https://code.visualstudio.com/) was used as the primary local Integrated Development Environment (IDE) for coding and development.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create a draft flowchart during the planning process.
- [ImgBB](https://imgbb.com/) was used to upload images and extract the source code.
- [Am I Responsive?](http://ami.responsivedesign.is) was used to generate the mockup of the website.
- [Table Convert](https://tableconvert.com/) was used to generate tables for the TESTING.md file.


## Testing

Testing information can be found in [TESTING.md file](TESTING.md).

## Deployment

Heroku was used to deploy the site. Here are the steps to deploy:

1. Log in to Heroku.
2. Click "Create a new app".
3. Choose the app name and region.
4. Click "Create app".
5. Navigate to the "settings" tab.
6. "Click "Reveal Config Vars".
7. Add a configuration variable to Heroku's Settings. The key is PORT and the value is 8000
8. Scroll down to "Buildpacks".
9. Click "Add Buildpack".
10. First, add "python" and click save.
11. Second, add "nodejs" and click save.

The live site can be found here: [The Italian Hangman Game]()

### Cloning:
1. Click the "Code" button in the GitHub repository.
2. Choose "HTTPS" and copy the URL.
3. Open the Terminam (in macOS) or Git Bash (in Windows) and navigate to the repository where you would like to locate the cloned repository.
4. Type "git clone" followed by the copied URL.
5. Press enter to create the clone.

### Forking
You can fork this project and make a copy of the original repository in your own GitHub account. In this case, you can view or make changes without affecting the original. To do so:

- log into GitHub and locate the GitHub Repository;
- at the top right of the screen, click the Fork button.

It should be noted that all changes pushed to the main branch are automatically reflected on the site.


## Credits
### Content
[TO BE ADDED]

### Code

As this was my first time building a game with [TO BE ADDED]

### Acknowledgment

I am very grateful to my mentor Brian Macharia for his suggestions, and to my classmate Niclas for his precious support. Also, a special thanks goes to the amazing tool that is Chat GBT: it helped me with the creation of the nursery rhyme (I give credit to myself as well here, as I've embellished and made the rhymes more meaningful), the debugging process and to better understand how Python works.