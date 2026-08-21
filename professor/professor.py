import random


def main():
    try:
        digits = get_level()

        correct = 0
        question = 0
        for question in range(10):
            x = generate_integer(digits)
            y = generate_integer(digits)
            equation = (f"{x} + {y} = ")

            print(equation, end="")
            attempt = 0
            while attempt < 3:
                try:
                    ans = int(input())
                    if ans == x + y:
                        correct += 1
                        break
                    else:
                        print("EEE")
                        attempt += 1
                        print(equation, end="")
                        ans
                except ValueError:
                    print("EEE")
                    attempt += 1
                    print(equation, end="")
                    continue

                if attempt == 3:
                    print(x + y)
                    break
        print(f"Score: {correct}")
    except EOFError:
        print("\nProgram terminated")


def get_level():
    while True:
        try:
            n = int(input("Level: "))

            if n == 1 or n == 2 or n == 3:
                return n
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        one_digit = random.randint(0, 9)
        return one_digit
    elif level == 2:
        two_digits = random.randint(10, 99)
        return two_digits
    elif level == 3:
        three_digits = random.randint(100, 999)
        return three_digits
    else:
        raise ValueError


if __name__ == "__main__":
    main()
