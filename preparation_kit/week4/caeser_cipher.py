#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    output = "" 
    for c in s:
        if(c >= 'A') and (c <= 'Z'):
            delta = ord(c) - ord('A') 
            delta = (delta + k) % 26 
            c = chr(ord('A') + delta) 
        elif(c >= 'a') and (c <= 'z'): 
            delta = ord(c) - ord('a') 
            delta = (delta + k)%26 
            c = chr(ord('a') + delta)
        output+=c
    return output

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
