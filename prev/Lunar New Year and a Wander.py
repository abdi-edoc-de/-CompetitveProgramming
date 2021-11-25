import sys
from heapq import heappop,heappush,heapify
from typing import DefaultDict
def solve(n,graph,edges,mn):
    heap = []
    heappush(heap,mn)
    visited = set()
    ret = []
    while heap:
        node = heappop(heap)
        if node in visited:
            continue
        ret.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                heappush(heap, neighbour)
    print(* ret)



def main():
    n , edges = list(map(int,input().split()))
    graph = DefaultDict(list)
    mn = sys.maxsize
    for _ in range(edges):
        prev , after = list(map(int,input().split()))
        graph[prev].append(after)
        graph[after].append(prev)
        mn = min(after,prev,mn)
    solve(n,graph,edges,mn)
main()
