#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counter = [0 for i in range(len(arr))]
    for bird in arr:
        counter[bird] +=1 
    max_sight = -99999
    bird_type = -1
    for elem in counter:
        if elem > max_sight:
            max_sight = elem
            bird_type = counter.index(max_sight)

    return bird_type

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
