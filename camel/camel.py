def main():
    snake_case = case_converter(input("camelCase: "))
    print("snake_case: ", snake_case)
    

def case_converter(words):
    snake = words[0]
    for char in words[1:]:
        if char.isupper():
            snake += "_"
        snake += char
    return snake.lower()


main()
