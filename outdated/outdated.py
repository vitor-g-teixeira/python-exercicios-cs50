def main():
    get_date()

def get_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        user_input = input("Date: ")
        countup = 0
        corresponded = False
        try:
            month, day, year = user_input.split("/", 3)
            year = int(year)
            month = int(month)
            day = int(day)
        except:
            try:
                month, day, year = user_input.split(" ", 3)
                if not day.endswith(","):
                    continue
                day = day.replace(",", "")
                day = int(day)
                for item in months:
                    countup += 1
                    if item == month:
                        corresponded = True
                        break
                month = countup
            except ValueError:
                pass
            else:
                if day <= 31 and corresponded:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        else:
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break

main()
