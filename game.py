"""A number-guessing game."""

# Put your code here
import random

def guessing_game():
    """Player guesses number between 1 nand 100"""

    player = input("What is your name? > ")

    print("Im going to think of a number between 1 and 100.")
    print("Guess the number!")

    secret_num = random.randint(1,100)
    # too_low=0
    # too_high=101
    guess = 102

    while secret_num != guess:
        guess = int(input("What number am I thinking of? > ".format(player)))

        if guess > secret_num:
            # too_high = guess
            print('This number is too high. ')

        elif guess < secret_num:
           # too_low = guess
           print('This number is too low.')

        else:
            print("You guessed it right! Good Job!")


guessing_game()