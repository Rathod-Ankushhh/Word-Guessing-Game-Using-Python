import random
def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
def hangman():
    secret_word = choose_word().lower()
    word_length = len(secret_word)
    guessed_letters = set()
    attempts_left = 7
    print("Welcome to Hangman!")
    print("Hint use vowels")
    print(f"The secret word has {word_length} letters.")
    print(display_word(secret_word, guessed_letters))
    print(f"You have {attempts_left} attempts left.")
    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in secret_word:
            print("Correct guess!")
            print(display_word(secret_word, guessed_letters))
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word:", secret_word)
                break
        else:
            attempts_left -= 1
            print(f"Incorrect guess. You have {attempts_left} attempts left.")
            print(display_word(secret_word, guessed_letters))
        if attempts_left == 0:
            print("You ran out of attempts!")
            print("The secret word was:", secret_word)
if __name__ == "__main__":
    hangman()
