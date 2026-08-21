import inflect

p = inflect.engine()

allNames = []
while True:
    try:
        name = input("Name: ")
        allNames.append(name)
    except EOFError:
        print("\n", end="")
        break


print("Adieu, adieu, to", p.join(allNames, conj="and"))
