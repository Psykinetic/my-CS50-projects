import pytest
from numb3rs import validate

def test_valid_IPv4():
    assert validate("1.1.1.1") == True
    assert validate("255.0.23.4") == True


def test_invalid_first_octet():
    assert validate("365.1.15.20") == False


def test_invalid_any_octet():
    assert validate("54.502.6.10") == False
    assert validate("54.22.638.10") == False
    assert validate("54.17.91.482") == False


def test_corner_cases():
    assert validate("192.168.001.1") == False


def test_not_an_IPv4():
    assert validate("cat") == False
