def main():
    greet = input("Greeting: ").lstrip().rstrip()
    print(value(greet))


def value(greeting):
    if greeting.startswith("Hello") or greeting.startswith("hello"):
        return 0
    elif greeting.startswith("H") or greeting.startswith("h"):
        if not greeting.startswith("Hello") or not greeting.startswith("hello"):
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()





