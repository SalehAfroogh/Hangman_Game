import random
import nltk
from nltk.corpus import words

# Make sure you have downloaded the 'words' corpus
nltk.download('words')

# Get a list of English words
word_list = words.words()

# Generate a random list of 10 words
random_words = random.sample(word_list, 10)

# Print the generated list of words
print(f"Generated list of words: {random_words}")

# Select one random word from the generated list of 10
random_word = random.choice(random_words).lower()  # Ensure it's in lowercase for comparison
word_length = len(random_word)  # Calculate the length of the selected word

# Print the final randomly selected word
print(f"The randomly selected word is: {random_word}")


# Initialize variables
hidden_word = ["-"] * word_length  # Represents the word with unguessed letters as "-"
remaining_guesses = word_length    # Total number of guesses is the length of the word
guessed_letters = set()            # Keep track of guessed letters

# Game loop
while remaining_guesses > 0:
    print(f"\nWord to guess: {' '.join(hidden_word)}")
    guess = input("Please enter a single letter: ").lower()

    # Validate the input
    if not (guess.isalpha() and len(guess) == 1):
        print("Invalid input. Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed the letter '{guess}'. Try a different one.")
        continue

    # Add the guessed letter to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guess is correct
    if guess in random_word:
        print(f"Good job! The letter '{guess}' is in the word.")
        # Reveal the guessed letter in the hidden word
        for i, letter in enumerate(random_word):
            if letter == guess:
                hidden_word[i] = guess.upper()
    else:
        print(f"Your guess '{guess}' is incorrect. Try again.")
        remaining_guesses -= 1

    # Check if the word has been completely guessed
    if "-" not in hidden_word:
        print(f"\nCongratulations! You've guessed the word: {''.join(hidden_word)}")
        print("You win!")
        break

    print(f"You have {remaining_guesses} guesses left.")

# If the user runs out of guesses
if "-" in hidden_word and remaining_guesses == 0:
    print(f"\nSorry, you lost! The word was: {random_word}. Better luck next time!")
