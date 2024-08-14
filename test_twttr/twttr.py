def main():
    phrase = input("")
    print(shorten(phrase))

def shorten(word):
    _output = word
    for _letter in _output:
        if is_vowel(_letter):
         _output = _output.replace(_letter, "")
    return _output

def is_vowel(_letter):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        if _letter == vowel:
            return True
    return False

if __name__ == "__main__":
    main()
