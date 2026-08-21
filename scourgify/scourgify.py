import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    students = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            last, first = name.split(", ")
            house = row["house"]
            students.append({"first": first, "last": last, "house": house})

    with open(sys.argv[2], "w") as newFile:
        writer = csv.DictWriter(newFile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
