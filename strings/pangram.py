#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    alphapet = "abcdefghijklmnopqrstuvwxyz "
    for each_char in alphapet:
        if each_char not in s:
            return "not pangram"
        
    return "pangram"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
