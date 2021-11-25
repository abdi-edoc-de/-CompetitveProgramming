import sys
from typing import DefaultDict
def solve(edges):
    graph = DefaultDict(list)
    limit = sys.maxsize()
    for i in edges:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))
        