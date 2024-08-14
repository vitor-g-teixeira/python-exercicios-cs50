import sys
import csv
from tabulate import tabulate

def main():
    prices = []
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    prices.append(row)
        except FileNotFoundError:
            sys.exit("File does not exist")

        print(tabulate(prices, headers="keys", tablefmt="grid"))
        print(prices)

main()
