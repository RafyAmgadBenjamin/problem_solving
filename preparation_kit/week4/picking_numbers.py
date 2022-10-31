#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    a.sort()
    window_count = 0
    max_window_count = 0
    window_min_val = -99999
    if a:
        window_min_val = a[0]
    else:
        return 0
    for i in range(len(a)-1):
        # window_min_val_
        if abs(window_min_val - a[i+1]) <= 1:
            window_count += 1
        else:
            if window_count > max_window_count:
                max_window_count = window_count
            window_count = 0
            window_min_val = a[i+1]
    if window_count > max_window_count:
        max_window_count = window_count
    return max_window_count + 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
