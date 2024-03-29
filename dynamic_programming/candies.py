#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def candies(n, arr):
    minArr1 = [1 for i in range(n)]
    minArr2 = [1 for i in range(n)]
    finalArr = []

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            minArr1[i] = minArr1[i - 1] + 1
        else:
            minArr1[i] = 1

    for j in range(len(arr) - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            minArr2[j] = minArr2[j + 1] + 1
        else:
            minArr2[j] = 1

    for i in range(len(arr)):
        finalArr.append(max(minArr1[i], minArr2[i]))

    return sum(finalArr)


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
