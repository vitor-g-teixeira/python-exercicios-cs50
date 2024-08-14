import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    first_hours = None
    second_hours = None
    if match := re.match(r"([0-9]+)(\:[0-9][0-9])? (AM|PM) to", s):
        if match.group(2) == None:
            first_minutes = ":00"
        else:
            first_minutes = match.group(2)

        if int(first_minutes.replace(":","")) / 60 >= 1 or int(match.group(1)) > 12:
            raise(ValueError)

        if match.group(3) == "PM" and match.group(1) != "12":
            first_hours = int(match.group(1)) + 12
        else:
            first_hours = int(match.group(1))
            if first_hours == 12 and match.group(3) == "AM":
                first_hours = 0
    else:
        raise(ValueError)
    if match_2 := re.match(r"(?:(?:[0-9]+)(?:\:[0-9][0-9])? (?:AM|PM) to) ([0-9]+)(\:[0-5][0-9])? (AM|PM)", s):
        if match_2.group(2) == None:
            second_minutes = ":00"
        else:
            second_minutes = match_2.group(2)

        if int(second_minutes.replace(":","")) / 60 >= 1  or int(match_2.group(1)) > 12:
            raise(ValueError)

        if match_2.group(3) == "PM" and match_2.group(1) != "12":
            second_hours = int(match_2.group(1)) + 12
        else:
            second_hours = int(match_2.group(1))
            if second_hours == 12 and match_2.group(3) == "AM":
                second_hours = 0
    else:
        raise(ValueError)

    if first_hours > 23 or second_hours > 23:
        raise(ValueError)

    return f"{first_hours:02}{first_minutes} to {second_hours:02}{second_minutes}"

if __name__ == "__main__":
    main()
