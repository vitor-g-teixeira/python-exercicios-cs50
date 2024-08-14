import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    typed_numbers = []

    if matches := re.match(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for match in matches.group(1, 2, 3, 4):
            typed_numbers.append(int(match))

        if all(0 <= number <= 255 for number in typed_numbers):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
