denomination = [25, 10, 5]
change = 50
while change > 0:
    print("Amount Due:", change)
    coin = int(input("Insert Coin:"))
    if coin in denomination:
        change -= coin


print("Change Owed:", 0 - change)
