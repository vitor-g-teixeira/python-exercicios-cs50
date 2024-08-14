suffix = input("File name: ").strip()
suffix = suffix.lower()

while("." in suffix):
    suffix = suffix.split(".", 1)[1]

if(suffix == "jpg"):
    suffix = "jpeg"

match(suffix):
    case "gif" | "jpeg" | "png":
        print("image/" + suffix)
    case "pdf" | "zip":
        print("application/" + suffix)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
