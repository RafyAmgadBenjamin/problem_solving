#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = {}
    pairs = dict((sock, 0) for sock in ar)
    pairs_count =  0
    for sock in ar:
        pairs[sock] += 1
        if pairs[sock] % 2== 0:
            pairs_count += 1 

    return pairs_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
