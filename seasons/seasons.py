from datetime import date
import sys
import inflect

def main():
        print(get_date(input("Date of birth: ")))

def get_date(given_date):
    try:
        year, month, day = given_date.split("-")
    except:
        sys.exit("Invalid Date")

    try:
        diff = date.today() - date(int(year), int(month), int(day))
    except:
         sys.exit("Invalid Date")

    minutes_alive = diff.days * 24 * 60
    inflecter = inflect.engine()
    return inflecter.number_to_words(minutes_alive, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()
