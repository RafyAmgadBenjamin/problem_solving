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
    arr.sort()
    min_diff = 9999999999999999999

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if min_diff > diff:
            min_diff = diff
    return min_diff

    # Write your code here
    # arr_len = len(arr)
    # min_diff = 9999999999999999999
    # for i in range(arr_len):
    #     for j in range(i + 1, arr_len):
    #         diff = abs(arr[i] - arr[j])
    #         if min_diff > diff:
    #             min_diff = diff
    # return min_diff


if __name__ == "__main__":

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
