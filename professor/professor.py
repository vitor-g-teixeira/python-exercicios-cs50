import random

def main():

    choosen_level = get_level()
    problems = generate_integer(choosen_level)
    tries = 3
    score = 0

    for problem in problems:
        while tries > 0:
            x, y = problem.split(" + ", 2)
            awnser = int(x) + int(y)
            user_awnser = input(problem + " =")
            try:
                user_awnser = int(user_awnser)
            except ValueError:
                pass

            if user_awnser != awnser:
                print("EEE")
                tries -= 1
            else:
                break

        if tries == 0:
            print(problem + " = ", awnser)
        else:
            score += 1
        tries = 3

    print("Score:", score)

def get_level():
    while True:
        try:
                user_level = int(input("Level: "))
                if 0 < user_level < 4:
                    return user_level
        except ValueError:
            pass


def generate_integer(level):
    problemList = []
    while len(problemList) < 10:
        if level == 1:
            lnumber_r = int(0)
        else:
            lnumber_r = int("1" + "0" * (level - 1))
        bnumber_r = int("9" * level)

        x = random.randint(lnumber_r, bnumber_r)
        y = random.randint(lnumber_r, bnumber_r)
        problem = str(x) + " + " + str(y)
        problemList.append(problem)
    return problemList

if __name__ == "__main__":
    main()
