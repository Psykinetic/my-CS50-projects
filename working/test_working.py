import pytest
from working import convert

def test_12hr_to_24hr():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("7:15 AM to 4:45 PM") == "07:15 to 16:45"
    assert convert("10:00 PM to 7 AM") == "22:00 to 07:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")


def test_omitting_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_omitting_AM_and_PM():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")



