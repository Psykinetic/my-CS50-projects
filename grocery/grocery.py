groceries = {
    #Vegetables
    "TOMATO": 1, "LETTUCE": 1, "CARROT": 1, "CELERY": 1, "ZUCHINNI": 1,
    "SQUASH": 1, "GREEN PEPPER": 1, "RED PEPPER": 1, "BANANA PEPPER": 1,
    "ONION": 1, "CORN": 1, "SPINACH": 1, "COLLARD GREEN": 1, "CUCUMBER": 1,
    "BROCCOLI": 1, "ASPARAGUS": 1, "GREEN BEAN": 1, "BEAN": 1,
    "CAULIFLOWER": 1, "KALE": 1, "POTATO": 1, "SWEET POTATO": 1,
    #Fruits
    "APPLE": 1, "BANANA": 1, "ORANGE": 1, "GRAPE": 1, "STRAWBERRY": 1,
    "CHERRY": 1, "MANGO": 1, "PINEAPPLE": 1, "PEAR": 1, "GRAPEFRUIT": 1,
    "DRAGONFRUIT": 1, "TANGERINE": 1, "NECTARINE": 1, "WATERMELON": 1,
    "PLUM": 1, "LEMON": 1, "LIME": 1, "KIWI": 1, "CANTALOPE": 1,
    "PEACH": 1, "AVOCADO": 1,
    #Meat
    "CHICKEN": 1, "BEEF": 1, "SAUSAGE": 1, "HAM": 1, "LAMB": 1,
    "TURKEY": 1,
    #Beverages
    "MILK": 1, "JUICE": 1, "WATER": 1,
    #Misc
    "BREAD": 1, "CHIPS": 1, "PASTA": 1, "TORTILLA": 1, "SUGAR": 1,
    "SALT": 1, "PEPPER": 1,
    #Sweets
    "COOKIE": 1, "ICE CREAM": 1, "PASTRY": 1
}

grocery_list = {}
while True:
    try:
        item = input("").upper()
        quantity = groceries.get(item)

        if item in groceries:
            if item in grocery_list:
                grocery_list[item] += 1
            elif item not in grocery_list:
                grocery_list[item] = 1
    except KeyError:
        print("\n", end="")
    except EOFError:
        print("\n", end="")
        break


final_list = sorted(grocery_list)

for item in final_list:
    print(f"{grocery_list.get(item)} {item}")
