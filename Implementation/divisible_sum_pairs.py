#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    ar_len = len(ar)
    for i in range(ar_len):
        j = i + 1
        while j < ar_len:
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
            j += 1
        i += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
