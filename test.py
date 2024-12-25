import unittest
from unittest.mock import patch
import random

# Mock the game code
class WordGuessingGameTest(unittest.TestCase):
    def setUp(self):
        # Example random word for testing
        self.random_word = "test"
        self.word_length = len(self.random_word)
        self.hidden_word = ["-"] * self.word_length
        self.remaining_guesses = self.word_length

    def test_word_selection(self):
        """Test that a random word is selected from a given list."""
        word_list = ["apple", "banana", "cherry"]
        random_word = random.choice(word_list)
        self.assertIn(random_word, word_list)

    def test_initial_hidden_word(self):
        """Test that the hidden word is initialized correctly."""
        expected_hidden_word = ["-"] * self.word_length
        self.assertEqual(self.hidden_word, expected_hidden_word)

    def test_correct_guess_updates_hidden_word(self):
        """Test that a correct guess updates the hidden word."""
        guess = "t"
        for i, letter in enumerate(self.random_word):
            if letter == guess:
                self.hidden_word[i] = guess.upper()
        self.assertEqual(self.hidden_word, ["T", "-", "-", "T"])

    def test_incorrect_guess_reduces_remaining_guesses(self):
        """Test that an incorrect guess reduces remaining guesses."""
        initial_remaining_guesses = self.remaining_guesses
        guess = "z"  # Incorrect guess
        if guess not in self.random_word:
            self.remaining_guesses -= 1
        self.assertEqual(self.remaining_guesses, initial_remaining_guesses - 1)

    @patch("builtins.input", side_effect=["t", "e", "s", "t"])
    def test_game_win(self, mock_input):
        """Test the game win condition."""
        random_word = "test"
        hidden_word = ["-"] * len(random_word)
        guessed_letters = set()
        remaining_guesses = len(random_word)

        while remaining_guesses > 0:
            guess = mock_input()
            guessed_letters.add(guess)
            if guess in random_word:
                for i, letter in enumerate(random_word):
                    if letter == guess:
                        hidden_word[i] = guess.upper()
            else:
                remaining_guesses -= 1
            if "-" not in hidden_word:
                break

        self.assertEqual("".join(hidden_word).lower(), random_word)

    @patch("builtins.input", side_effect=["a", "b", "c", "d", "e"])
    def test_game_loss(self, mock_input):
        """Test the game loss condition."""
        random_word = "test"
        hidden_word = ["-"] * len(random_word)
        guessed_letters = set()
        remaining_guesses = len(random_word)

        while remaining_guesses > 0:
            guess = mock_input()
            guessed_letters.add(guess)
            if guess in random_word:
                for i, letter in enumerate(random_word):
                    if letter == guess:
                        hidden_word[i] = guess.upper()
            else:
                remaining_guesses -= 1
            if "-" not in hidden_word:
                break

        self.assertNotEqual("".join(hidden_word).lower(), random_word)

if __name__ == "__main__":
    unittest.main()
