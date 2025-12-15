from src.calculator import add, subtract, divide
import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)