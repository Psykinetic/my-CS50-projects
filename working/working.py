import re

def main():
    try:
        print(convert(input("Hours: ").strip()))
    except ValueError:
        raise ValueError


def convert(s):
    twelve = re.search(r"^([1-9]|1[0-2]):?([0-5][0-9])?[ ](AM|PM)[ ]to[ ]([1-9]|1[0-2]):?([0-5][0-9])?[ ](AM|PM)$", s)
    if twelve:
        hour1 = int(twelve.group(1))
        minute1 = twelve.group(2)
        hour2 = int(twelve.group(4))
        minute2 = twelve.group(5)

        if twelve.group(3) == "PM" and hour1 < 12:
            hour1 = hour1 + 12

        if twelve.group(6) == "PM" and hour1 < 12:
            hour2 = hour2 + 12

        if twelve.group(3) == "AM" and hour1 == 12:
            hour1 = 0

        if twelve.group(6) == "AM" and hour2 == 12:
            hour2 = 0

        if minute1 == None:
            minute1 = "00"

        if minute2 == None:
            minute2 = "00"

        return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
