#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    min_dif = 9999999999999999
    arr.sort()
    for i in range(len(arr)-1):
        dif_elem = abs(arr[i]- arr[i+1])
        if dif_elem < min_dif:
            min_dif = dif_elem
    return min_dif 
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         dif_elem = abs(arr[i]-arr[j])
    #         if dif_elem < min_dif:
    #             min_dif = dif_elem
    # return min_dif


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
