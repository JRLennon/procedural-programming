import pytest
from exercise03 import *

def test_two_list_different_size():
    assert common_elements([1,2,3,4], [3,4,19,21,5]) == [3,4]

def test_no_common_elements():
    assert common_elements([3,3,3], [4,4,4]) == []

def test_all_elements_common():
    assert common_elements([3,4,5],[3,4,5]) == [3,4,5]

def test_two_common_elements():
    assert common_elements([11,10,9,23],[23,11,15]) == [11,23]

def test_pos_neg():
    assert common_elements([-11,11,-9,10,8],[10,-3,0,14,8,-9]) == [-9,8,10]

pytest.main()