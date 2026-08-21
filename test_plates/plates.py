def main():
    plate = input("Plate: ").capitalize()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    def length_2_to_6(s):
        if len(s) >= 2 and len(s) <= 6:
            return True
    def starts_with_2_letters(s):
        if s[0:2].isalpha():
            return True
        else:
            return False
    def is_alphanumeric(s):
        if s.isalnum() and starts_with_2_letters(s) and len(s) >= 3:
            return True
        else:
            return False
    def is_all_letters(s):
        if s.isalpha():
            return True
        else:
            return False
    def first_num_not_0(s):
        for char in s:
            if char.isdigit():
                if char != "0":
                    return True
                else:
                    return False
        return False
    def ends_with_num(s):
        for i, char in enumerate(s):
            if char.isdigit():
                digit_1 = i
                break
        if s[digit_1:].isdigit():
            return True
        else:
            return False


    if length_2_to_6(s) and is_alphanumeric(s) and first_num_not_0(s) and ends_with_num(s):
        return True
    elif length_2_to_6(s) and is_all_letters(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
