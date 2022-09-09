### NUMBER GUESSING GAME ###

# step 1 - get the guess from the user and reflect it back
# step 2 - generate a secret random number
# step 3 - make the guessing logic repeat until the game is over
# step 4 - limit max guesses to 6
# step 5 - (bonus round) - output the user's guess history and number of guess attempts

from ctypes.wintypes import HINSTANCE
import random

secret_number = random.randint(1, 100)
max_attempts = 6
guess_history = []

for attempts in range(max_attempts):
    guess = int(input("Welcome to the guessing game. Please enter your guess: "))
    guess_history.append(guess)
    print(f"You guessed {guess}")

    if int(guess) > secret_number:
        print("Your guess is too high")

    elif guess < secret_number:
        print("Your guess is too low")

    if guess == secret_number:
        break

if guess == secret_number:
    print(f"You guessed the secret number: {secret_number} in {attempts} guesses. You win!")
else:
    print(f"You ran out of guesses. The secret number was: {secret_number}")

def print_history(guesses):
    print("\nGuess History:\n")
    for index in range(len(guesses)):
        print(f"Guess #{index + 1}: {guesses[index]}")

print_history(guess_history)

print("\nThanks for playing!")
