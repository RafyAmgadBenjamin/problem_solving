#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count_list = [1, 1, 1, 1]
    for single_char in password:

        if single_char in "0123456789":
            count_list[0] -= 1

        elif single_char in "abcdefghijklmnopqrstuvwxyz":
            count_list[1] -= 1

        elif single_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count_list[2] -= 1

        elif single_char in "!@#$%^&*()-+":
            count_list[3] -= 1

    # GET total number of changes needed

    total = 0
    needed_char=0
    for count in count_list:
        if count <= 0:
            continue
        else:
            total += count
    # Check if it need more character to reach 6 
    if total + n < 6:
        needed_char = 6 - (total + n)

    return total + needed_char


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)

    # fptr.write(str(answer) + '\n')

    # fptr.close()
