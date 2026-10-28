import random

number = random.randint(1,100)
attempts = 0
max_attempts = 7

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 100.")
print("You have {} attempts!".format(max_attempts))

while attempts < max_attempts:
    try:
        guess_input = int(input("Enter a guess:"))

    except ValueError:
        print("Invalid input, Enter a whole number between 1-100")
        continue

    if guess_input < 1 or guess_input > 100:
        print("Invalid number! Enter a number between 1 and 100.")
        continue  # Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.

    attempts = attempts+1

    if guess_input == number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    elif guess_input < number:
        print("Too Low! Try a higher number.")
        print(f"You have {max_attempts-attempts} left")
    
    else:
        print("Too High! Try a lower number.")
        print(f"You have {max_attempts-attempts} left")
    


else:
    print(f"Game Over! The correct number was {number}.")

