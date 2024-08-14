def main():
    currentTime = input("What time it is? ")

    currentTime = convert(currentTime)

    if currentTime == "7.5":
        print(currentTime)

    if 7 <= currentTime <= 8:
        print("breakfast time")
    elif 12 <= currentTime <= 13:
        print("lunch time")
    elif 18 <= currentTime <= 19:
        print("dinner time")

def convert(time):
    _hours, _minutes = time.split(":", 2)
    _hours = float(_hours)
    _minutes = float(_minutes)
    time = _hours + (_minutes/60)
    return time

if __name__ == "__main__":
    main()

