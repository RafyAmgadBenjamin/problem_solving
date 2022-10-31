#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here

    i = j = 0
    count = 0
    st = "SOS"
    while i < len(s):
        if s[i] != st[j]:
            count += 1
        i += 1
        if i % 3 == 0:
            j = 0
        else:
            j += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
