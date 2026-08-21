from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("RACECAR") == "RCCR"


def test_punctuation():
    assert shorten(",.!?") == ",.!?"


def test_numbers():
    assert shorten("1234") == "1234"


if __name__ == "__main__":
    main()
