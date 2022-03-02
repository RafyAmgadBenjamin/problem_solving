#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    # values = random(len(arr)+1)
    arr.insert(0, -1)
    swap_counter = 0
    for i in range(1, len(arr)):
        while arr[i] != i:
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp
            # arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
            swap_counter += 1
    return swap_counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
