import pytest
from exercise11 import *

def test_word_generation(): # check that the program can actually generate a secret word, and is not empty/returning a failure
    assert generate_secret_word() != ""

def test_hint_list_generation(): # check that you can generate a word, and then create a hint list from it
    assert generate_hint_letter_list(generate_secret_word())

pytest.main()