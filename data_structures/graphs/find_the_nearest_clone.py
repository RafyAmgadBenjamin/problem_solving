#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(set)

    def add_edge(self,src, dest):
        self.edges[src].add(dest)
        self.edges[dest].add(src)


def BFS_shortest_path(start,graph: Graph):
    distance = [-1] * (len(graph.nodes)+1)
    distance[start] = 0
    Q = deque()
    Q.appendleft(start)
    while Q:
        node = Q.pop()
        for neigh in graph.edges[node]:
            if distance[neigh] == -1:
                distance[neigh] = distance[node] + 1
                Q.appendleft(neigh)
    return distance




def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    graph = Graph()
    graph.nodes = range(1, graph_nodes+1)
    index = 0
    while index < len(graph_from):
        graph.add_edge(graph_from[index],graph_to[index])
        index += 1
    
    # color_index = ids.index(val)

    # color_index = -1
    # for i in range(len(ids)):
    #     if ids[i] == color:
    #         color_index = i
    color_index = -1
    if val in ids:
        color_index = ids.index(val)
    else:
        return color_index

    distances = BFS_shortest_path(graph.nodes[color_index],graph)
    
    min_dist = 999999999
    # for i in range(color_index,len(graph.nodes)):
    for i in range(color_index+1,len(ids)):
        if ids[i] == val: # node have the desired color
            if distances[i+1] < min_dist:
                min_dist = distances[i+1]

    return min_dist if min_dist != 999999999 else -1



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print(ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
