#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    counters = [0,0,0]
    for elem in arr:
        if elem> 0:
            counters[0]+=1 #postive
        elif elem<0:
            counters[1]+=1 #negative
        else:
            counters[2]+=1 

    print('{0:.6f}'.format(counters[0]/len(arr)))
    print('{0:.6f}'.format(counters[1]/len(arr)))   
    print('{0:.6f}'.format(counters[2]/len(arr)))   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
