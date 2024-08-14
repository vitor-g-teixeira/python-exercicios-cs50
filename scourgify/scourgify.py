import sys
import csv

def main():
    students = []
    first_names = []
    last_names = []

    if len(sys.argv) == 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    for student in students:
        lastn, firstn = student["name"].split(",", 2)
        first_names.append(firstn.strip())
        last_names.append(lastn)

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for firstn, lastn, house in zip(first_names, last_names, students):
            writer.writerow({"first": firstn, "last": lastn, "house": house["house"]})

main()
