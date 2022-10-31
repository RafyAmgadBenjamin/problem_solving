

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


# def balancedSums(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return("YES")
#     return("NO")

def balancedSums(arr):
    left=0
    right=sum(arr[1:])
    if left==right: return "YES"
    for i in range(len(arr)-1):
        if left==right: return "YES"
        left +=arr[i]
        right -=arr[i+1]
    return "NO"
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()
