#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    counter = 0
    valleys_counter = 0
    mountain_counter = 0
    mount = False
    valley= False
    for step in path:
        if step == "U":
            counter += 1
        else:
            counter -= 1

        if counter > 0 :
            mount = True

        elif counter < 0: 
            valley= True
        elif counter == 0 and mount: 
            mountain_counter+=1
            mount= False
        elif counter == 0 and valley:
            valleys_counter +=1
            valley == False
    return valleys_counter 
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
