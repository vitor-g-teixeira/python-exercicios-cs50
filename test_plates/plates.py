import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    position = 0
    length = len(s) - 1
    numExist = False

    for letter in s:

        if position <= 1 and letter.isnumeric():
            return False
        elif letter in string.punctuation:
            return False

        if letter.isnumeric() and not numExist:
            if int(letter) == 0:
                return False
            else:
                numExist = True

        if numExist and not letter.isnumeric():
            return False

        if length > 5 or length < 1:
            return False

        position += 1

    return True


if __name__ == "__main__":
    main()
