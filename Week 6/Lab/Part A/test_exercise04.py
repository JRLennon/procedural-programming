import pytest
from exercise04 import *

def test_one_adult_10am():
    assert movie_ticket_price(0,1,0,10) == 14.25

def test_two_children_two_adult_5pm():
    assert movie_ticket_price(2,2,0,17) == 30

def test_two_children_two_adults_1pm():
    assert movie_ticket_price(2,2,0,13) == 28.50

def test_two_children_one_adult_one_senior_1pm():
    assert movie_ticket_price(2,1,1,13) == 30.40

def test_three_children_two_adults_one_senior_2pm():
    assert 38.94 < movie_ticket_price(3,2,1,14) < 38.96

def test_three_children_one_adult_two_seniors_3pm():
    assert movie_ticket_price(3,1,2,15) == 49

def test_four_children_three_adults_two_seniors_11am(): # Failing ... figure out later
    assert movie_ticket_price(4,3,2,11) == 69.35

def test_negative_01():
    assert movie_ticket_price(-2,5,6,2) == None

def test_negative_02():
    assert movie_ticket_price(2,-5,6,2) == None

def test_negative_03():
    assert movie_ticket_price(2,5,-6,2) == None

def test_negative_04():
    assert movie_ticket_price(2,5,6,-2) == None

pytest.main()