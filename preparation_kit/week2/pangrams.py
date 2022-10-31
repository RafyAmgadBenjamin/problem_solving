#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    letters = dict((key, False) for key in string.ascii_lowercase)
    s = s.lower()
    for ch in s: 
        letters[ch] = True
    if False in letters.values():
        return "not pangram"
    return "pangram"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
