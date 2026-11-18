import pytest
from exercise02 import *

def test_fibonacci_iterative():
    assert fibonacci_iterative(15) == 610

def test_fibonacci_recursive():
    assert fibonacci_recursive(15) == 610

pytest.main()
