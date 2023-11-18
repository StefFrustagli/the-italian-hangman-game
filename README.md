# THE ITALIAN HANGMAN GAME

*It's time to play the **Italian hangman game**!*</br>
</br>
This is a Python terminal game that runs on Heroku's mock terminal created by the Code Institute.

This game is intended for intermediate Italian learners and Italians speakers (children or adults) who enjoy simple word guessing games. As the instructions are given in English, a basic understanding of English is also required. It is a classic version of the game in which the player must guess the word, letter by letter, within a certain number of attempts.

View the live project [here](https://the-italian-hangman-game-c1a71b18c016.herokuapp.com/).

Responsive Mockup:
![Responsive Mockup](https://i.ibb.co/H2p6wRc/responsive-mockup.png) 

## Table of Contents

- [User Experience (UX)](#user-experience)
- [Planning ](#Planning)
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

## Planning
### Flowchart
I created this flowchart when I was planning the logic for the game. Even though it is rough and does not contain all the passages, it has helped me with the development of the game dynamic.

![Draft flowchart](https://i.ibb.co/9Y6gmWv/my-screenshots-2023-11-18-at-18-19-32.png)

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
The goal of the game is to identify the word correctly within seven attempts and save the little man from execution. As a way of simplifying the guessing game, I have defined three different categories the player can choose from at the beginning.

### Existing Features

#### Introduction
When the terminal is open, a classic picture of the Hangman game is displayed.

![Hangman picture](https://i.ibb.co/fdnQFxj/hangman-pic.png)

Afterwards, a message welcoming the player is accompanied by a nursery rhyme that gives a jolly introduction to the game. As an alternative to the usual rules list, I came up with something that tries to grab the user's attention.

![Welcome message and nursery rhyme](https://i.ibb.co/7189q62/Welcome-message-and-rhyme.png)

After that, the user is given a line of instructions with the number of attempts they have to guess the word. This is followed by an invitation to play, in capital letters, to which the user can reply and start the game dynamic.

![Instruction line and nvitation to play](https://i.ibb.co/wKmZqZt/my-screenshots-2023-11-17-at-20-30-20.png)

##### Introductory nursery rhyme 

The nursery rhyme was created with chatGPT collaboration. I think it's my favourite part since it sets a merry atmosphere. As this type of game is very straightforward, the rhyme was just a funny way for me to convey the most important pieces of information. Reading it, the player can learn what the game is about (guessing a word), the language of the word (Italian), and the game's purpose (saving a little man from the Italian hangman) that gives a little bit of extra funny context.

#### User interactions 

The game begins when the player enters 'yes'. Immediately, they are asked to choose a category from "Natural phenomena," "Months & seasons," and "Animals."

![Select a category: 1: Natural phenomena, 2: Months & seasons, 3: Animals](https://i.ibb.co/mFSbyhS/category.png)

When the player selects a category, the Italian translation appears, followed by a dashed word with dashes corresponding to the letters the player must guess. Next is the input for guessing a letter. 

![Dashboard when category is selected](https://i.ibb.co/XsQyWNZ/my-screenshots-2023-11-18-at-15-09-14.png)

Whenever a correct letter is guessed, it replaces the dashes in the word and a "well done!" message is displayed.

The dashboard will appear like this:
![Dashboard when correct letter is guessed](https://i.ibb.co/BBbYPxF/well-done-correct-letter.png)


When a wrong letter is guessed, instead, a consequent message informing the player appears. A piece of the Hangman picture and the remaining attempts are displayed accordingly.

The dashboard will appear like this:
![Dashboard when wrong letter is guessed](https://i.ibb.co/3zwxD0k/The-letter-is-not-in-the-word.png)

The game continues until the attempts are over or the player guesses the word first.

##### Phases of the hangman's picture
Since the user has seven chances to guess the word, seven pieces of the Hangman picture will be constructed, one by one. Whenever the user makes a wrong guess, this is displayed. 

Image displayed when the attempts left are 6:
![Image displayed when the attempts left are 6](https://i.ibb.co/kxyJWMP/attempts-6.png)

Image displayed when the attempts left are 5:
![Image displayed when the attempts left are 5](https://i.ibb.co/7rZpB1M/my-screenshots-2023-11-18-at-12-57-37.png)

Image displayed when the attempts left are 4:
![Image displayed when the attempts left are 4](https://i.ibb.co/5cYrnM0/my-screenshots-2023-11-18-at-14-13-57.png)

Image displayed when the attempts left are 3:
![Image displayed when the attempts left are 3](https://i.ibb.co/GTN0Dnh/my-screenshots-2023-11-18-at-12-58-16.png)

Image displayed when the attempts left are 2:
![Image displayed when the attempts left are 2](https://i.ibb.co/7pJkqDk/my-screenshots-2023-11-18-at-12-59-33.png)

Image displayed when the attempt left is 1:
![Image displayed when the attempt left is 1](https://i.ibb.co/DkDRpzy/my-screenshots-2023-11-18-at-12-59-59.png)

Image displayed when the attempt left is 0:
![Image displayed when the attempt left is 0](https://i.ibb.co/NYsgM5v/my-screenshots-2023-11-18-at-13-00-27.png)


##### Victory message
A victory message appears when the player wins the game:
![Victory message](https://i.ibb.co/VjCcDCz/victory-message.png)

##### Loss message
A loss message appears when the player loses the game:
![Loss message](https://i.ibb.co/bzhPsm7/loss-message.png)

##### Restart the game
A restart input appears whenever the player wins or loses. 
![Input to restart the game](https://i.ibb.co/TwVGJRt/Would-you-like-to-play-again-input.png)
An affirmative answer restarts the game and the player is asked to select a category. A negative answer ends the game.


##### Exit the game
Whenever the player responds negatively to the game-starting input, the game is ended and a goodbye message appears.
![Game exits](https://i.ibb.co/VDPmzkL/would-you-like-to-play-again-NO.png)

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
This is a classic Hangman game with Italian words. For more info about the history of the game, please refer to [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)).

### Code

My first step was to watch some hangman videos on YouTube, like [this](https://youtu.be/cJJTnI22IF8?si=4nZef1AhFSj1baPk) by Kylie Ying or [this one](https://youtu.be/m4nEnsavl6w?si=Wi3xwg5GOtgJFG6m) by Kite, to get an idea of how to set the game up. Then in preparation for coding, I created a flowchart to visualize the game logic. When the logic was clear, I started writing function descriptions as my mentor suggested so I would know exactly what I wanted from each function. Then I coded step-by-step, aided by online researching.

### Acknowledgment

I am very grateful to my mentor Brian Macharia for his suggestions, and to my classmate Niclas for his precious support. Also, a special thanks goes to the amazing tool that is ChatGPT: it helped me with the creation of the nursery rhyme (I give credit to myself as well here, as I've embellished and made the rhymes more meaningful), the debugging process and to better understand how Python works.