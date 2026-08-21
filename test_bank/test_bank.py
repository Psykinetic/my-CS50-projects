from bank import value

def test_hello():
    assert value("Hello") == 0


def test_h_not_hello():
    assert value("Howdy") == 20


def test_not_h():
    assert value("What's up") == 100


if __name__ == "__main__":
    main()
