def main():
    phrase = input("Input: ")
    tweet = turn_into_tweet(phrase)

    print("Output: ", tweet, sep="")

def turn_into_tweet(_phrase):
    _output = _phrase
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

main()
