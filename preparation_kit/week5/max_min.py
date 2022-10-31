#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    lowest_fairness = 9999999999999999
    for i in range(0,len(arr)-k+1):
        fairness_val = arr[i+k-1]- arr[i]
        if fairness_val < lowest_fairness:
            lowest_fairness = fairness_val
    return lowest_fairness

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
