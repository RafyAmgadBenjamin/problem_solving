#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # pass
    # Write your code here
    swap_count = 0
    array_len = len(a)
    for i in range(array_len):
        for j in range(array_len - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_count += 1
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]} ")
    print(f"Last Element: {a[array_len-1]}  ")


if __name__ == "__main__":
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
