import random

words = ["apple", "world", "python", "mango", "tree","sachin"]
secret_word = random.choice(words)

guessed_letters = set()
attempts = 6

print("===== WORD GUESSING GAME =====")
print("Guess the hidden word!")
print(f"The word contains {len(secret_word)} letters.")
print(f"You have {attempts} incorrect guesses available.")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower().strip()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print(f"Attempts remaining: {attempts}")

if all(letter in guessed_letters for letter in secret_word):
    print("\nYOU WIN!")
else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)