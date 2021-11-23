#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(set)


def bfs(node, g, used: set):
    Q = deque()
    Q.appendleft(node)
    size = 1
    while Q:
        cur = Q.pop()
        for neigh in g.edges[cur]:
            if neigh in used:
                continue
            used.add(neigh)
            Q.appendleft(neigh)
            size += 1
    return size, used


def count_cluster(g: Graph):
    n_clusters = 0
    used = set()
    csize = []
    for node in g.nodes:
        if node in used:
            continue
        size, used = bfs(node, g, used)
        n_clusters += 1
        csize.append(size)

    return n_clusters, csize


def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib <= c_road:
        return c_lib * n

    g = Graph()

    g.nodes = range(1, n + 1)

    for a, b in cities:
        g.edges[a].add(b)
        g.edges[b].add(a)

    n_clusters, csize = count_cluster(g)
    return n_clusters * c_lib + sum((cluster_nodes - 1) * c_road for cluster_nodes in csize)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)

        fptr.write(str(result) + "\n")

    fptr.close()

# 1
# 3 3 2 1
# 1 2
# 3 1
# 2 3

# 1
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6
