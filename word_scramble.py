# word_scramble.py

import random

# List of words for the game
words = ["python", "programming", "algorithm", "developer", "keyboard", "variable", "function", "loop", "dictionary"]

# Function to scramble the letters of a word
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Main game function
def play_game():
    print("Welcome to the Word Scramble Game!")
    score = 0

    for word in words:
        scrambled = scramble_word(word)
        print(f"\nScrambled word: {scrambled}")

        # Get the player's guess
        guess = input("Your guess: ")

        # Check the guess
        if guess == word:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct word was: {word}")

    print(f"\nGame Over! Your score: {score}/{len(words)}")

# Start the game
if __name__ == "__main__":
    play_game()
