#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    db = {}
    db[0], db[1] = arr[0], max(arr[0], arr[1])
    for i, val in enumerate(arr[2:], start=2):
        db[i] = max(db[i - 1], db[i - 2] + val, val)
    return db[len(arr) - 1] if db[len(arr) - 1] > 0 else 0


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
