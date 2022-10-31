#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    # Write your code here
    numbers = {ele: 0 for ele in brr}
    for i in brr:
        if i in  numbers:
            numbers[i] += 1
        else:
            numbers[i] = 1
    for i in arr:
        numbers[i] = numbers[i] - 1
    result = []
    for key, val in numbers.items():
        if val != 0:
            result.append(key)
    result.sort()
    return  result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
