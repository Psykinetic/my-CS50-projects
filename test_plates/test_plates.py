from plates import is_valid

def test_plates_alphanumeric():
    assert is_valid("ABC123") == True


def test_plates_starts_with_0():
    assert is_valid("ABC012") == False


def test_plates_not_alphanumeric():
    assert is_valid("AB12!") == False


def test_plates_numeric_only():
    assert is_valid("1234") == False


def test_plates_end_with_letter():
    assert is_valid("AB123C") == False


def test_plates_too_long():
    assert is_valid("ABCD1234") == False


def test_plates_too_short():
    assert is_valid("A") == False


if __name__ == "__main__":
    main()
