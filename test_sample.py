# tests/test_sample.py
import pytest
from calculator import add

@pytest.fixture
def sample_data():
    return {"a": 2, "b": 3, "expected": 5}

def test_add(sample_data):
    assert add(sample_data["a"], sample_data["b"]) == sample_data["expected"]

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (0, 0, 0), (-1, 1, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
