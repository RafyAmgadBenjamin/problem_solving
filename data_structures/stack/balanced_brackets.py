#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    stack = deque()
    brackets = {}
    brackets[")"] = "("
    brackets["]"] = "["
    brackets["}"] = "{"
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        else:
            if not stack or brackets[ch] != stack.pop():
                return "NO"
    if stack:  # handle this case {{{{
        return "NO"
    return "YES"
    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()


## Test Case
# 6
# }][}}(}][))]
# [](){()}
# ()
# ({}([][]))[]()
# {)[](}]}]}))}(())(
# ([[)

# output
# NO
# YES
# YES
# YES
# NO
# NO
