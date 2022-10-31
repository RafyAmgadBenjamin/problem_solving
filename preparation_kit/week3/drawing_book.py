#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    all_book = n - 1 # except the first page 
    double_pages = math.ceil(all_book/2)
    double_pages_cover = double_pages + 1  
    no_flips  = double_pages_cover -1 
    front_flips =  math.floor(p/2)
    return front_flips if no_flips - front_flips > front_flips else  no_flips - front_flips

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
