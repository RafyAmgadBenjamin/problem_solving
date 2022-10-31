#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    my_grid = []
    for st in grid:
        temp_arr = list(st)
        temp_arr.sort()
        my_grid.append(temp_arr)
    
    for i in range(len(my_grid[0])-1):
        for j in range(len(my_grid)-1):
            if my_grid[j][i] > my_grid[j+1][i]:
                return "NO"
                
    return "YES"

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
    
# 1
# 3
# a b c
# a d e
# e f g

# 1
# 3
# a b c
# a a e
# e f g