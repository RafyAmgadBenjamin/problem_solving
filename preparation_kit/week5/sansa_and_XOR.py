#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from functools import reduce

def sansaXor(arr):
    if len(arr)%2 == 0:
        return 0
    return eval("^".join(str(arr[i]) for i in range(0, len(arr), 2)))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
