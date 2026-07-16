import pytest

from function import Operation, calc


# --- sum ---

def test_sum_positive_integers():
    assert calc(3, 4, Operation.SUM) == 7


def test_sum_negative_numbers():
    assert calc(-2, -3, Operation.SUM) == -5


def test_sum_floats():
    assert calc(1.5, 2.5, Operation.SUM) == pytest.approx(4.0)


def test_sum_with_zero():
    assert calc(0, 5, Operation.SUM) == 5


# --- sub ---

def test_sub_positive_integers():
    assert calc(10, 4, Operation.SUB) == 6


def test_sub_result_negative():
    assert calc(3, 7, Operation.SUB) == -4


def test_sub_floats():
    assert calc(5.5, 2.2, Operation.SUB) == pytest.approx(3.3)


# --- mul ---

def test_mul_positive_integers():
    assert calc(3, 4, Operation.MUL) == 12


def test_mul_by_zero():
    assert calc(99, 0, Operation.MUL) == 0


def test_mul_negative_numbers():
    assert calc(-3, 4, Operation.MUL) == -12


def test_mul_floats():
    assert calc(2.5, 4.0, Operation.MUL) == pytest.approx(10.0)


# --- div ---

def test_div_exact():
    assert calc(10, 2, Operation.DIV) == 5.0


def test_div_float_result():
    assert calc(7, 2, Operation.DIV) == pytest.approx(3.5)


def test_div_negative_dividend():
    assert calc(-9, 3, Operation.DIV) == pytest.approx(-3.0)


def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        calc(5, 0, Operation.DIV)


def test_div_zero_divided_by_nonzero():
    assert calc(0, 5, Operation.DIV) == pytest.approx(0.0)
