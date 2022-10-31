#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    bits = f'{n:032b}'
    new_bits = ""
    for bit in bits:
        if bit == "0":
            new_bits += "1"
        else:
            new_bits += "0"
    return int(new_bits,2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
