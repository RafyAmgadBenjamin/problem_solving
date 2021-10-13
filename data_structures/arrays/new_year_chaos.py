#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    moves = 0
    for i, p in enumerate(q):
        if p - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(p - 2, 0), i + 1):
            if q[j] > p:
                moves += 1
    print(moves)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
