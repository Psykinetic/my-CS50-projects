import pytest
from um import count


def test_isolated_um():
    assert count("um") == 1
    assert count("Um, what?") == 1
    assert count("Um, thanks, um...") == 2


def test_words_with_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Given the circumstances...") == 0
    assert count("This is cumbersome.") == 0
