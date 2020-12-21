#!/bin/python3

import math
import os
import random
import re
import sys
   

def handle_small_letter_rotations(ascii_new_val):
    # Handling rotations in small letter
    if ascii_new_val > 122:
        diff =  ascii_new_val - 122
        ascii_new_val = 97 + (diff -1)
    return ascii_new_val

def handle_capital_letter_rotations(ascii_new_val):
    # Handling rotation in capital letter
    if ascii_new_val > 90:
        diff =  ascii_new_val - 90
        ascii_new_val = 65 + (diff -1)
    return ascii_new_val



# Complete the caesarCipher function below.
def caesarCipher(s, k):
    # removing full rounds
    while k > 26:
        k=k-26

    cipher_str = ""
    for each_char in s:
        ascii_val = ord(each_char)
        ascii_new_val = -1
        # capital letter
        if ascii_val >=65 and ascii_val <= 90:
            ascii_new_val = ascii_val + k  
            ascii_new_val = handle_capital_letter_rotations(ascii_new_val)
            cipher_str += chr(ascii_new_val)

        # small letter
        elif ascii_val >=97 and ascii_val <= 122:
            ascii_new_val = ascii_val + k  
            ascii_new_val = handle_small_letter_rotations(ascii_new_val)
            cipher_str += chr(ascii_new_val)

        else:
            cipher_str+=each_char
            continue
    return cipher_str
        
            

if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(result)