import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    if ums := re.findall(r"\b(?: )?(um)(?: )?\b", s, flags = re.IGNORECASE):
        print(ums)
        return len(ums)
    else:
        return 0


if __name__ == "__main__":
    main()
