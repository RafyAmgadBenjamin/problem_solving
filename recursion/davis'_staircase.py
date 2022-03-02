#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
from collections import defaultdict
def stepPerms(n):
    values = defaultdict(int)
    def stepCount(n,values):
        if n == 1:
            return 1
        if  n ==2 :
            return 2
        if n == 3 : 
            return 4
        if values[n]:
            return values[n]
        else:
            values[n] = stepCount(n-1,values) + stepCount(n-2,values) + stepCount(n-3,values)
            return values[n]
          
        
    
    return stepCount(n,values)

# def stepPerms(n):
#     count = 0
#     def stepCount(n):
#         # nonlocal count
#        nonlocal count
#        if n == 0:
#            count += 1
#            return
#        if n<0:
#            return
#        stepCount(n-1)
#        stepCount(n-2)
#        stepCount(n-3)
    
#     stepCount(n)
#     return count


    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)
        print(res)

        # fptr.write(str(res) + '\n')

    # fptr.close()
