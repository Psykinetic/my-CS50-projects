def main():
    while True:
        try:
            fuel = fraction_to_percent(input("Fraction: "))
            if 99 <= fuel <= 100:
                print("F")
                break
            elif 1 < fuel < 99:
                print(f"{fuel}%")
                break
            elif 0 <= fuel <= 1:
                print("E")
                break
        except ValueError:
            print("A non-integer character was entered")
        except ZeroDivisionError:
            print("Denominator must be greater than 0")


def fraction_to_percent(fraction):
    x, y = map(int, fraction.split("/"))
    fraction = float((x / y) * 100)
    return round(fraction)


main()
