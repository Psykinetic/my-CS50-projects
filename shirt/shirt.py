import sys
import os
from PIL import Image, ImageOps

try:
    valid_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    path1 = sys.argv[1]
    root1, ext1 = os.path.splitext(path1)
    path2 = sys.argv[2]
    root2, ext2 = os.path.splitext(path2)
    if ext1 not in valid_extensions:
        sys.exit("Invalid input")
    elif ext2 not in valid_extensions:
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")


    with Image.open(sys.argv[1]) as image:
        image = ImageOps.fit(image, (600, 600))
        shirt = Image.open("shirt.png")
        image.paste(shirt, shirt)
        image.save(sys.argv[2])


except FileNotFoundError:
    sys.exit(f"Input does not exist")
