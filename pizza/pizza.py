import csv
import sys
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    with open(sys.argv[1], "r") as file:
        table = csv.DictReader(file)

        print(tabulate(table, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit(f"{sys.argv[1]} does not exist")

