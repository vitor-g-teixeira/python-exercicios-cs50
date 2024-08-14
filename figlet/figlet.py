from pyfiglet import Figlet
import sys
import random

font_options = Figlet().getFonts()

if len(sys.argv) == 1:
    font_name = random.choice(font_options)
    f = Figlet(font=font_name)
    message = input("Input: ")
    print(f.renderText(message))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        countdown = len(font_options)

        for font_name in font_options:
            if sys.argv[2] == font_name and countdown != 0:
                f = Figlet(font=font_name)
                break
            elif countdown != 0:
                countdown -= 1
        if countdown == 0:
            sys.exit("Invalid usage")
        else:
            message = input("Input: ")
            print(f.renderText(message))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
