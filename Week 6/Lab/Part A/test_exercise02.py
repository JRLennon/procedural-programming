import pytest
from exercise02 import *

def test_random():
    assert alphabetical_sort("programming") == "aggimmnoprr"

def test_different_letters():
    assert alphabetical_sort("civic") == "cciiv"

def test_already_sorted():
    assert alphabetical_sort("aabb") == "aabb"

def test_capital_small():
    assert alphabetical_sort("PaBaBB") == "aaBBBP"

def test_mix_uppercase_lowercase():
    assert alphabetical_sort("BaAaA") == "aaAAB" # i think there is a typo in the lab document here? swapped it to aaAAB like the rest of them follow

pytest.main()
