import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("99/100") == 99
    assert convert("1/2") == 50
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_noninteger_value():
    with pytest.raises(ValueError):
        convert("cat")


def test_negative_integer_value():
    with pytest.raises(ValueError):
        convert("-1/10")


def test_divisor_less_than_quotient():
    with pytest.raises(ValueError):
        convert("3/2")


if __name__ == "__main__":
    main()
