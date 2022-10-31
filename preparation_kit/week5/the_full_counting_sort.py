#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

# def countSort(arr):
#     half_arr_len = int(len(arr)/2)
#     prev_arr  = [ x[1] for x in arr]
#     arr.sort(key=lambda x:(x[0], x[1]))
#     final_str = ""
#     for ele in arr : 
#         if ele[1] in prev_arr[0: half_arr_len]:
#             final_str += "-"
#         else:
#             final_str += ele[1]
#         final_str+= " "
#     print(final_str.strip())
def countSort(arr):
    maxIdx = max([int(row[0]) for row in arr])
    results = [[] for _ in range(maxIdx + 1)]
    
    left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
    
    for idx, val in left:
        results[int(idx)] += ['-']
    
    for idx, val in right:
        results[int(idx)] += [val]
         
    results = " ".join([" ".join(result) for result in results if len(result) > 0])
    print(results)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
# case 1
# 4   
# 0 a
# 1 b
# 0 c 
# 1 d