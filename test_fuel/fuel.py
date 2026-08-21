def main():
    try:
        fuel = convert(input(""))
        print(gauge(fuel))
    except ValueError:
        print("Value Error")
    except ZeroDivisionError:
        print("Cannot divide by 0")


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    fraction = float((x / y) * 100)
    if fraction < 0 or fraction > 100:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        return int(round(fraction))

def gauge(percentage):
    if 99 <= percentage <= 100:
        return f"F"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    elif 0 <= percentage <= 1:
        return f"E"


if __name__ == "__main__":
    main()
