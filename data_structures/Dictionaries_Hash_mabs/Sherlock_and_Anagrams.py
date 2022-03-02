#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


from collections import Counter
def get_substring(s: str):
    substrings = []
    str_len = len(s)
    for i in range(str_len+1):
        for j in range(i+1, str_len+1):
            sub_sorted = ""
            sub = s[i:j]
            sub_sorted = ''.join(sorted(sub))
            substrings.append(sub_sorted)

    return substrings


def sherlockAndAnagrams(s):
    substrings = get_substring(s)

    anagrams = {}
    counter = 0
    for sub in substrings:
        if not sub in anagrams:
            anagrams[sub] = 1
        else:
            counter += anagrams[sub]
            anagrams[sub] +=1
    return counter
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
