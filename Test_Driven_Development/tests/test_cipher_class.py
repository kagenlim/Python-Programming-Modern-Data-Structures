#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pytest

# In[ ]:
def cipher(text, shift, encrypt=True):  # modified cipher
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if type(shift) == str:
            raise Exception("Please enter an integer value for the shift argument.")
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index + 1]  # if encrypt is False, shift will not happen
    return new_text


@pytest.fixture(name='cipher')
def cipher_fixture():
    return cipher()


def test_single_word():
    result = cipher('bob', 1)
    expected = 'cpc'  # expected result, should the test pass
    assert result == expected


def test_lowercase_only():
    result = cipher('prince', 1)
    expected = 'qsjodf'  # expected result, should the test pass
    assert result == expected


def test_uppercase_only():
    result = cipher('BOB', 1)
    expected = 'CPC'  # expected result, should the test pass
    assert result == expected


def test_sentence_with_spaces():
    result = cipher('Bob hit the prince', 1)
    expected = 'Cpc iju uif qsjodf'  # expected result, should the test pass
    assert result == expected

# In[ ]:

@pytest.mark.parametrize("text, shift, expected", [
    ('bob', 1, 'cpc'),
    ('fun', -1, 'etm'),
    ('b%b', 1, 'c%c'),
    ('BOB', 1, 'CPC'),
    ('john', 'two', Exception)
])
class TestCipher:
    def test_cipher_with_single_word(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected

    def test_ciper_negative_shift(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected

    def test_cipher_non_alphabet(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected

    def test_uppercase_only(self, text, shift, expected):
        actual = cipher(text, shift)
        assert actual == expected

    def test_string_string_shift(self, text, shift, expected):
        with pytest.raises(Exception):
            cipher(text, shift)