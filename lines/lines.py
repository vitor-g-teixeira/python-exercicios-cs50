import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    user_input = sys.argv[1]
    user_input = user_input.lstrip(user_input[:-3])
    line_amount = 0

    if user_input != ".py":
        sys.exit("Not a python file.")

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.strip().startswith("#") and line.strip() != "":
                    line_amount += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_amount)

main()
