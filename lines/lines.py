import sys

count = 0

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

    for line in lines:
        current_line = line.lstrip()

        if current_line.startswith("#"):
            continue
        elif current_line == "":
            continue
        else:
            count += 1

    print(count)

except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} does not exist")



