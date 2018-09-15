import random

def play_game():
    print("Howdy, what's your name?")

    name = input(">")

    random_number = random.randint(1, 101)


    num_guess = 1


    while True:
        guess = (input("Guess a number between 1 and 100 please "))

        try:
            guess = int(guess)
            if guess > 100 or guess <1:
                print ("learn to read!!!")
                #guess = int(input("Guess a correct number this time "))


            elif guess != random_number:

                if guess > random_number:
                    print("Guess too high")

                elif guess < random_number:
                    print("Guess too low")

               # guess = int(input("Guess again please "))
                num_guess += 1

            else:
                if num_guess == 1:
                    print("Congrats! You guessed correctly in {} try".format(num_guess))
                    break
                else:
                    print("Congrats! You guessed correctly in {} tries".format(num_guess))
                    break

        except ValueError:
            print("Guess a number please ")









play_game()