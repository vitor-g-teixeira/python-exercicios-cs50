def main():

    user_input = input("Digit in camelCase: ")
    print(to_snake_case(user_input))

def to_snake_case(_word):
    _output = ""
    for _letter in _word:
        if _letter.isupper():
            _output += "_" + _letter.lower()
        else:
            _output += _letter
    return _output

main()
