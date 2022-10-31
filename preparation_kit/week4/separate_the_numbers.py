#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):

    res = 'NO'

    for i in range(len(s)):
        starting_digit = int(s[: i + 1])
        new_s = str(starting_digit)

        if len(new_s) != len(s):
            digit = starting_digit
            while len(new_s) < len(s):
                digit += 1
                new_s += str(digit)

            if new_s == s:
                res = f"YES {starting_digit}"
                break

    print(res)


    # Write your code here
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
