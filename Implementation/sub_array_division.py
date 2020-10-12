#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    possibilities = 0
    list_len = len(s)
    if list_len != 1:
        for i in range(list_len):
            j = i + 1
            total = s[i]
            count = 1
            while j < list_len:
                count += 1
                total += s[j]
                if total == d:
                    if count == m:
                        possibilities += 1
                    break
                elif total < d:
                    j += 1
                else:
                    break

        return possibilities
    else:
        if d == s[-1] and m == 1:
            return m
        else:
            return 0


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
