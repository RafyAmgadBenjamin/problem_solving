#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    # d = defaultdict(int)
    # for index, elem in enumerate(cost):
    #     d[elem] = index + 1

    # for val in cost:
    #     if money >= val:
    #         rest = money - val
    #         if d[rest] > 0:
    #             print(f"{d[val]} {d[rest]}\n")
    #             return
    # costs = [-1] * (len(cost) + 1)
    # for val in cost:
    #     costs[val] = val

    # for val in cost:
    #     if money >= val:
    #         rest = money - val
    #         if d[rest] != -1:
    #             print(f"{costs.index(val)} {costs.index(rest)}\n")
    #             return
    remains = {}
    for index, val in enumerate(cost):
        if not val not in remains:
            remains[money - val] = index + 1  # index of the first value
        else:
            print(remains[val], index + 1)  # index here is the second value
    # Write your code here


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

# 1
# 5
# 5
# 2 1 3 5 6

# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
