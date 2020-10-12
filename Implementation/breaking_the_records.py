#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    min_val = scores[0]
    max_val = scores[0]
    min_count = 0
    max_count = 0
    for item in scores:
        if min_val > item:
            min_count += 1
            min_val = item
        if max_val < item:
            max_count += 1
            max_val = item
    return max_count, min_count


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

    # fptr.write(" ".join(map(str, result)))
    # fptr.write("\n")

    # fptr.close()
