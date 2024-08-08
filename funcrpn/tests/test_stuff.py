"""Unit tests"""

from funcrpn import __main__


def test_detect():
    "Unit test"
    assert __main__.detect_type("0.12333") == (0.12333, __main__.NUMBER)
    assert __main__.detect_type("3") == (3, __main__.NUMBER)
    assert __main__.detect_type("+") == ("+", __main__.OPERATOR)
