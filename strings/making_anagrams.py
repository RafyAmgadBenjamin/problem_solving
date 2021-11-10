#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def makeAnagram(a, b):
    a_counter = Counter(a)
    b_counter = Counter(b)
    deletions_count = 0
    for val in a_counter.keys():
        res = b_counter[val] - a_counter[val]
        if res >= 0:
            b_counter[val] -= a_counter[val]
        else:
            # if b_counter[val]:  # there is value for b
            deletions_count += abs(res)
            b_counter[val] = 0
    deletions_count += sum(b_counter.values())
    return deletions_count

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()
