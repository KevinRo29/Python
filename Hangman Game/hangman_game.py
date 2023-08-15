import random

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

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    print("Welcome to Hangman Game!")

    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 8

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect! You have {} attempts left.".format(attempts))

        if display_word(word_to_guess, guessed_letters) == word_to_guess:
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("\nGame over! The word was:", word_to_guess)
            break

if __name__ == '__main__':
    hangman()
            