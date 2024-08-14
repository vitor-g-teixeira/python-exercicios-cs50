import sys

def main():
    fuel_percentage = convert(input("Fraction: "))
    print(gauge(fuel_percentage))

def convert(fraction):
        try:
            x, y = fraction.split("/", 2)
        except ValueError:
            raise ValueError
        
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x <= y:
            return round((x/y) * 100)
        else:
            raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
