#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    i=j=0
    first_diag = 0
    while i< len(arr):
        while j < len(arr[i]):
            first_diag+= arr[i][j]
            break;
        j += 1
        i += 1
    
    j = len(arr)-1
    i = 0
    second_diag = 0
    while i < len(arr):
        while j >= 0:
            second_diag+= arr[i][j]
            break
        i += 1
        j -= 1
    
    return abs(first_diag - second_diag)








if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
