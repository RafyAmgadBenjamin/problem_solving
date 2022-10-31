#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    changes_count = 0
    password = set(password)
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = "!@#$%^&*()-+"
    if not password.intersection(numbers):
        changes_count += 1
    if not password.intersection(lower_case):
        changes_count += 1
    if not password.intersection(upper_case):
        changes_count += 1
    if not password.intersection(special_characters):
        changes_count += 1
    if n < 6:
        if n + changes_count > 6:
            return changes_count
        else:
            dif = 6 - (n + changes_count)
            return changes_count + dif
    return changes_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)

    # fptr.write(str(answer) + '\n')

    # fptr.close()
