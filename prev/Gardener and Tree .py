
from collections import defaultdict, deque
from os import rename
from typing import DefaultDict

def solve(edges , op):
    # print(edges)
    # print(op)
    graph = defaultdict(set)
    indegree = defaultdict(int)
    parent = [-1] * (len(edges) + 2)
    
    leafs = set()
    if len(edges) <= op:
        print(0)
        return
    for i in edges:
        graph[i[1]].add(i[0])
        graph[i[0]].add(i[1])
        parent[i[1]] = i[0]
    for i in graph:
        indegree[i] = len(graph[i]) - 1
        if indegree[i] == 0 :
            leafs.add(i)
    
    deletedNode = 0
    for i in range(op):
        temp = set()
        for k in leafs:
            cur = graph[k].pop()
            indegree[cur] -= 1
            if indegree[cur] == 0:
                temp.add(cur)
        deletedNode += len(leafs)
        leafs = temp
    print(len(edges) +1 - deletedNode)
    

def main():
    t = int(input())
    for i in range(t):
        input()
        arr = list(map(int,input().split()))
        vert = arr[0]
        op = arr[1]
        edges = []
        for k in range(vert-1):
            edges.append(list(map(int,input().split())))
        solve(edges,op)


main()

