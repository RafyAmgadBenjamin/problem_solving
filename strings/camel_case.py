#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count = 1
    for single_char in s :
        if single_char.isupper():
            count+=1
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
