import pytest
from exercise01 import *

def test_pos():
    assert calc(3, 4) == 12

def test_neg():
    assert calc(-9, -4) == 36

def test_mix():
    assert calc(6, -3) == -18

def test_zero_left():
    assert calc(-4, 0) == 0

def test_zero_right():
    assert calc(0, 4) == 0

def test_non_numeric(): # this one should fail with a TypeError - added basic try except here
    assert calc("abc", "xyz") == None

pytest.main()
