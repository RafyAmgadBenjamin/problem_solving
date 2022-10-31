#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr_pairs = []
    arr.sort()
    min_dif = 9999999999
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) == min_dif:
            arr_pairs.append(arr[i])
            arr_pairs.append(arr[i+1])
        elif abs(arr[i]-arr[i+1]) < min_dif:
            arr_pairs = []
            arr_pairs.append(arr[i])
            arr_pairs.append(arr[i+1])
            min_dif = abs(arr[i]-arr[i+1])
    return arr_pairs




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
