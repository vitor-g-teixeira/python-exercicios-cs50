# Defining main
def main():
    # Getting input from user
    userInput = input("")
    # Converting the emoticons into emojis
    userInput = convert(userInput)
    # Printing the result
    print(userInput)

def convert(emoticon):
    # if there is a :) it will be substituted by a :) emoji
    emoticon = emoticon.replace(":)", "🙂")
    # if there is a :( it will be substituted by a :( emoji
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

main()
