def main():
    meal = convert(input("What time is it? "))

    if meal >= 7.00 and meal <= 8.00:
        print("breakfast time")
    elif meal >= 12.00 and meal <= 13.00:
        print("lunch time")
    elif meal >= 18.00 and meal <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    time = hours + minutes / 60
    return time


if __name__ == "__main__":
    main()



