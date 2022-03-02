#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
# from collections import defaultdict, Counter


# def freqQuery(queries):

#     # vals = defaultdict(int)
#     vals = Counter()
#     freqs = defaultdict(set)
#     res = []
#     for query in queries:
#         instr, val = query
#         current_freq = vals[val]
#         if instr == 1:
#             # remove the old freq
#             freqs[current_freq].discard(val)

#             vals[val] = current_freq + 1
#             # add the new freq
#             # new_freq = vals[val]
#             freqs[current_freq + 1].add(val)

#         elif instr == 2:
#             # remove the old freq
#             freqs[current_freq].discard(val)

#             vals[val] = current_freq -1
#             # add the new freq
#             # new_freq = vals[val]
#             freqs[current_freq -1].add(val)

#         elif instr == 3:
#             if freqs[val] and val:
#                 res.append(1)
#             else:
#                 res.append(0)
#     return res
from collections import Counter,defaultdict

def freqQuery(queries):
    c = Counter()
    d = defaultdict(set)
    for x,y in queries:
        v = c[y]
        if x==1:
            d[v].discard(y)
            d[v+1].add(y)
            c[y] = v+1
        elif x==3:
            yield 1 if d[y] else 0
        elif v:
            d[v].discard(y)
            d[v-1].add(y)
            c[y] = v-1
            
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
