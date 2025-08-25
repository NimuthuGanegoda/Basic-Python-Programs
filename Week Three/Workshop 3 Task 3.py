# Name: Nimuthu Ganegoda
# Student ID: 10695889

import random  # Import random module for generating random numbers

# Generate a random number between 1 and 1000 for the user to guess
number = random.randint(1, 1000)
# Initialize guess counter to track number of guesses
guess_counter = 0

print("Guess the number between 1 and 1000!")  # Prompt user to start guessing

guess = None  # Initialize guess variable
while guess != number:
    # Prompt user to enter a guess and convert input to integer
    guess = int(input("Enter your guess: "))
    # Increment guess counter each time user makes a guess
    guess_counter += 1
    # If guess is less than the number, inform user it's too low
    if guess < number:
        print("Too low!")
    # If guess is greater than the number, inform user it's too high
    elif guess > number:
        print("Too high!")
    # If guess is correct, congratulate user and show number of guesses
    else:
        print(guess, "is correct, you win!")
        print("You got it in", guess_counter, "guesses.")