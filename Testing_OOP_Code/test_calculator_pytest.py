# test_calculator_pytest.py

import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5

def test_subtract():
    assert calc.subtract(5, 3) == 2

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

# Run karne ke liye:
# pytest test_calculator_pytest.py
