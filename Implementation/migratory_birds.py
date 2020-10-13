#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr_counter = [0] * 6
    for item in arr:
        arr_counter[item] += 1

    max_val = -999999999
    max_index = -1
    for index, item in enumerate(arr_counter):
        if item > max_val:
            max_val = item
            max_index = index
    return max_index


# do array of counters with size 6 and add in each index related to the number
# find the maximum while tracking the first index.

if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
