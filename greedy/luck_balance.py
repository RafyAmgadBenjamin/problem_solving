#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    total_sum = 0
    important_scores = []
    for contest in contests:
        total_sum += contest[0]
        if contest[1] == 1:
            important_scores.append(contest[0])
    if k >= len(important_scores):
        return total_sum
    else:
        no_negelected = len(important_scores) - k
        important_scores.sort()
        for i in range(no_negelected):
            total_sum -= important_scores[i] * 2
    return total_sum

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
# 3 2
# 5 1
# 1 1
# 4 0


# 6 3
# 5 1
# 2 1
# 1 1
# 8 1
# 10 0
# 5 0
