# Hangman: Word Guessing Game
A simple Python-based command-line word guessing game where players try to guess a randomly selected word letter by letter within a limited number of attempts. The game is both entertaining and a great example of basic Python programming logic.

## Features
Random Word Selection: The game selects a random word from a list of 10 randomly generated words.
Interactive Gameplay: Users guess letters, and the game provides feedback on correct or incorrect guesses.
Dynamic Word Display: The guessed letters are revealed in their correct positions while unguessed letters remain hidden.
Guess Limitation: The number of guesses is equal to the length of the selected word.
Win or Lose Conditions:
Players win by guessing all the letters correctly within the allowed attempts.
Players lose if they fail to guess the word within the allowed attempts.

## Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/word-guessing-game.git
cd word-guessing-game
Install Dependencies:

The game uses the nltk library to generate random English words.
Install the required library:
bash
Copy code
pip install nltk
Download NLTK Data:

Ensure you have the words corpus downloaded:
bash
Copy code
python -c "import nltk; nltk.download('words')"

## How to Play
Run the game script:

bash
Copy code
python guess_word.py
Follow the prompts to guess the word:

Enter a single letter as your guess.
If the letter is correct, its position(s) in the word will be revealed.
If the letter is incorrect, you will lose one of your remaining guesses.
Keep guessing until:

You reveal the entire word (win).
You run out of guesses (lose).

## Testing
To ensure the game works as expected, unit tests are provided. Run the tests using unittest:

bash
Copy code
python -m unittest test_word_game.py


## Project Structure
bash
<img width="428" alt="Screenshot 2024-12-25 at 10 35 05 AM" src="https://github.com/user-attachments/assets/565ea5fe-7b2c-4d4c-93b2-079cec37a8c1" />





Fork the repository.
Create a new branch for your feature/bugfix.
Commit your changes and submit a pull request.



