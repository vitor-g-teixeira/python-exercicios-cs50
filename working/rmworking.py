import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.match(r"([0-2]?[0-9])(\:([0-5][0-9]))? ([A|P]M) to ([0-2]?[0-9])(\:([0-5][0-9]))? ([A|P]M)", s):

        if match.group(2) != None:
            first_minutes = match.group(2)
        else:
            first_minutes = ":00"

        if match.group(6) != None:
            second_minutes = match.group(6)
        else:
            second_minutes = ":00"

        hour_list = time_convertion(match.group(1), match.group(4), match.group(5), match.group(8))

        first_hour = hour_list[0]
        second_hour = hour_list[1]

        return f"{first_hour:02}{first_minutes} to {second_hour:02}{second_minutes}"
    else:
        raise ValueError

def time_convertion(first_hour, first_ampm, second_hour, second_ampm):
    first_hour = int(first_hour)
    second_hour = int(second_hour)

    if first_hour > 12 or second_hour > 12:
        raise ValueError

    if first_hour != 12 and first_ampm == "PM":
        first_hour = int(first_hour) + 12
    elif first_hour == 12 and first_ampm == "AM":
        first_hour = 0

    if second_hour != 12 and second_ampm == "PM":
        second_hour = int(second_hour) + 12
    elif second_hour == 12 and second_ampm == "AM":
        second_hour = 0

    return [first_hour, second_hour]

if __name__ == "__main__":
    main()
