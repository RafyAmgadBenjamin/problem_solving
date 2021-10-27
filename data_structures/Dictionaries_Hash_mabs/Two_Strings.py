#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


# def twoStrings(s1, s2):
#     d1 = {}
#     for i in range(len(s1) + 1):
#         for j in range(i + 1, len(s1) + 1):
#             sub = s1[i:j]
#             d1[sub] = 0
#     for i in range(len(s2) + 1):
#         for j in range(i + 1, len(s2) + 1):
#             sub = s2[i:j]
#             if sub in d1:
#                 d1[sub] += 1
#     for item in d1.items():
#         print(item)

#     sub_count = 0
#     for item in d1.values():
#         sub_count += item
#     return "YES" if sub_count > 0 else "NO"
def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"


if __name__ == "__main__":
    q = int(input().strip())
    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()
