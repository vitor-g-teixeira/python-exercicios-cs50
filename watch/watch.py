import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r"src=\"(?:https?://)?(?:www\.)?(youtube\.com/embed/\w+)\"", s):
        output = "https://" + matches.group(1).replace("be.com/embed/", ".be/")
        return output
    else:
        return None

if __name__ == "__main__":
    main()
