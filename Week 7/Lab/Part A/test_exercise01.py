import pytest
from exercise01 import *

def test_factorial_iterative():
    assert factorial_iterative(5) == 120

def test_factorial_recursive():
    assert factorial_recursive(5) == 120

pytest.main()

# tested with 1,3,5,7 - all returned correct values