import random

# Function to choose a random word from a list of words
def choose_random_word():
    words = [
        'python',
        'computer',
        'apple',
        'microsoft',
        'linux',
        'keyboard',
        'mouse',
        'CocaCola'
    ]
    return random.choice(words).upper()

# Function to display the word with the letters guessed correctly
def display_word(word, guessed_letters): 
    display = '' # Variable to store the word with the letters guessed correctly
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Function to play the game
def hangman():
    print("Welcome to Hangman Game!")

    word_to_guess = choose_random_word() # Variable to store the word to guess
    guessed_letters = [] # List to store the letters guessed by the user
    attempts = 8 # Variable to store the number of attempts

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters)) # Display the word with the letters guessed correctly
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha(): # Check if the user entered a single letter
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters: # Check if the user already guessed that letter
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess) # Add the letter to the list of guessed letters

        if guess in word_to_guess: # Check if the letter is in the word
            print("Correct!")
        else: # If the letter is not in the word, decrease the number of attempts
            attempts -= 1
            print("Incorrect! You have {} attempts left.".format(attempts))

        if display_word(word_to_guess, guessed_letters) == word_to_guess: # Check if the user guessed the word
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("\nGame over! The word was:", word_to_guess)
            break

if __name__ == '__main__':
    hangman()
            