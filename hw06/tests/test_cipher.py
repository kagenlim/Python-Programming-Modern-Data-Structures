#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pytest

# In[ ]:

def cipher(text, shift, encrypt=True):
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
            new_text += alphabet[new_index:new_index+1] #if encrypt is False, shift will not happen
    return new_text

# In[ ]:


def test_cipher_with_single_word():
    actual = cipher('bob', 1)
    expected = 'cpc' #expected result, should the test pass
    assert actual == expected
    
test_cipher_with_single_word()
##AssertionError was not raised, test passes


# In[ ]:


def test_ciper_negative_shift():
    actual = cipher('fun', -1)
    expected = 'etm'
    assert actual == expected
    
test_ciper_negative_shift()
##AssertionError was not raised, test passes, negative shift works


# In[ ]:


def test_cipher_non_alphabet():
    actual = cipher('b%b', 1)
    expected = 'c%c'
    assert actual == expected
    
test_cipher_non_alphabet()
##AssertionError was not raised, test passes, non-alphabetic symbols works; but function still processes alphabetic characterrs


# In[ ]:


def test_string_string_shift(): 
    with pytest.raises(Exception):
        cipher('john', 'two')

