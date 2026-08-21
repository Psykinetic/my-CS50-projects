greet = input("Greeting: ").lstrip().rstrip()


if greet.startswith("Hello") or greet.startswith("hello"):
    print("$0")
elif greet.startswith("H") or greet.startswith("h"):
    if not greet.startswith("Hello") or not greet.startswith("hello"):
        print("$20")
else:
    print("$100")
