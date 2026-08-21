def main():
    tweet = shorten(input("Input: "))
    print("Output:", tweet)


def shorten(word):
    vowels = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")

    newWord = ""
    for char in word:
        if char not in vowels:
            newWord += char
    return newWord


if __name__ == "__main__":
    main()
