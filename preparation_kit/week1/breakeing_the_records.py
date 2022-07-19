#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    standardScore = scores[0]
    maxScore = standardScore
    minScore = standardScore
    maxScoreCount = 0 
    minScoreCount = 0
    for score in scores : 
        if score> maxScore:
            maxScoreCount+=1
            maxScore = score
        if score < minScore:
            minScoreCount+=1
            minScore = score
    
    return [maxScoreCount, minScoreCount]
    
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
