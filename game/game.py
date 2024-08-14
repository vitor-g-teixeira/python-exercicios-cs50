import random
import sys

def main():
    user_level = -1
    while True:
        try:
            if not user_level > 0 :
                user_level = int(input("Level: "))

            if user_level > 0:
                guess = random.randint(1, user_level)
                user_guess = -1
                while guess != user_guess:
                    user_guess = int(input("Guess: "))

                    if user_guess > guess:
                        print("Too large!")
                    elif user_guess < guess and user_guess > 0:
                        print("Too small!")
                    elif user_guess > 0:
                        print("Just right!")
                        sys.exit()
        except ValueError:
            pass
main()
