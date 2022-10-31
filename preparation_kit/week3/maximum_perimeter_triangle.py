#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort(reverse=True)
    i = 0
    while i < len(sticks)-2:
        a = sticks[i]
        b = sticks[i+1]
        c = sticks[i+2]
        if a < b + c:
            return (c, b, a)
        i += 1
    return [-1]


    # max_prop = []   # prem, longest_max_side, longest_min_side
    # max_prem = -99999
    # longest_max_side = -9999
    # longest_min_side = -9999
    # longest_max_side = 0
    # longest_min_side = 0
    # index_of_max_prem = -1
    # final_triangle = []
    # for triangle in triangles:
    #     prem = sum(triangle)
    #     max_side = triangle[2]
    #     min_side = triangle[0]
    #     if prem < max_prem:
    #         continue
    #     elif prem > max_prem:
    #         max_sum_prem = prem
    #         longest_max_side= max_side
    #         longest_min_side = min_side
    #         index_of_max_prem = triangle.index(triangle)
    #     elif prem == max_sum_prem and max_side > longest_max_side:
    #         max_sum_prem = prem
    #         longest_max_side= max_side
    #         longest_min_side = min_side
    #         index_of_max_prem = triangle.index(triangle)
    #     elif prem == max_sum_prem and max_side > longest_max_side and min_side > longest_min_side:
    #         max_sum_prem = prem
    #         longest_max_side= max_side
    #         longest_min_side = min_side
    #         index_of_max_prem = triangle.index(triangle)
    #     elsif
    # for


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
