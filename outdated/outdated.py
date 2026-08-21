month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").title()

        if "/" in date:
            mm, dd, yyyy = map(int, date.split("/"))
            if mm >= 0 and mm <= 12 and dd >= 0 and dd <= 31:
                print(f"{yyyy}-{mm:02}-{dd:02}")
                break

        elif " " in date and ", " in date:
            for m in month:
                if m in date:
                    mm = int(month.index(m) + 1)
                    break
            for i, d in enumerate(date):
                if d.isdigit():
                    dg1 = str(d)
                    if date[i + 1].isdigit():
                        dg2 = str(date[i + 1])
                        dd = int(dg1 + dg2)
                    else:
                        dd = int(dg1)
                    break
            yyyy = date[-4:]
            if dd >= 0 and dd <= 31 and date[0:2].isalpha():
                print(f"{yyyy}-{mm:02}-{dd:02}")
                break
    except KeyError:
        print("\n", end="")
    except ValueError:
        print("\n", end="")
    except EOFError:
        print("\n", end="")
        break
