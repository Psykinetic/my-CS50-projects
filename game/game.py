import random


while True:
    try:
        max = int(input("Level: "))

        if max > 0:
            answer = random.randint(1, max)
            break
        else:
            print("", end="")
    except ValueError:
        print("", end="")


while True:
    try:
        guess = int(input("Guess: "))

        if guess > answer:
            print("Too large!")
        elif guess < answer and guess > 0:
            print("Too small!")
        elif guess == answer:
            print("Just right!")
            break
        else:
            print("", end="")
    except ValueError:
        print("", end="")


