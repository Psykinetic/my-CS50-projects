import validators

def main():
    email = input("What's your email address? ")
    test = validators.email(email)

    if test == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
