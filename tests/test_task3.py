from task2 import get_sqrt


def test_sqrt_good():
    assert get_sqrt(121) == 11


def test_sqrt_bad():
    assert get_sqrt(122) is None


def test_sqrt_negative():
    assert get_sqrt(-111) is None


def test_sqrt_zero():
    assert get_sqrt(0) == 0
