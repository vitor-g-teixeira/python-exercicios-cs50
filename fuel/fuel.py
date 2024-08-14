def main():
    current_fuel = get_fuel()
    if current_fuel <= 1:
        print("E")
    elif current_fuel >= 99:
        print("F")
    else:
        print(current_fuel, "%", sep="")

def get_fuel():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/", 2)
            x = int(x)
            y = int(y)
            if x <= y:
                return round((x/y) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
main()
