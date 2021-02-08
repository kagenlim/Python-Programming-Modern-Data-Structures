#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pytest

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

# In[ ]:

@pytest.mark.parametrize("shift", [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
])

def test_cipher_encrypt_decrypt(shift):
    encrypted = cipher('tom', shift, encrypt = True)
    decrypted = cipher(encrypted, -(shift), encrypt = True)
    assert decrypted == 'tom'

