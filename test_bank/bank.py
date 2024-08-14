def main():
    user_input = input("Greeting: ")
    print(value("$" + user_input))

def value(greeting):
    if greeting[0:5] == "hello" or greeting[0:5] == "HELLO":
        return 0
    elif greeting[0] == "H" or greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
