import sys
from PIL import Image
from PIL import ImageOps

def main():

    extensions = (".jpg", ".jpeg", ".png")

    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(extensions) or not sys.argv[2].endswith(extensions):
        sys.exit("Invalid input")

    finput_ext = sys.argv[1].split(".")[-1]
    sinput_ext = sys.argv[2].split(".")[-1]

    if finput_ext != sinput_ext:
        sys.exit("Input and output have different extensions")

    image_shirt = Image.open("shirt.png")
    image_before = Image.open(sys.argv[1])
    image_before = ImageOps.fit(image=image_before, size=image_shirt.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    image_before.paste(image_shirt, image_shirt)

    image_before.save(sys.argv[2])

main()
