import random

def play_game():
    print("Howdy, what's your name?")

    name = input(">")

    random_number = random.randint(1, 101)

    guess = int(input("Guess a number between 1 and 100 please"))

    num_guess = 1

    while True:
        if guess != random_number:

            if guess > random_number:
                print("Guess too high")

            else:
                print("Guess too low")

            guess = int(input("Guess again please "))
            num_guess += 1

        else:
            print("Congrats! You guess correctly in {} tries".format(num_guess))
            break

play_game()