from collections import deque
from typing import DefaultDict


def main():
    arr = list(map(int,input().split()))
    nodes = arr[0]
    dest = arr[1]

    portals = list(map(int,input().split()))

    graph = DefaultDict(list)
    n= len(portals)
    for i in range(n):
        graph[i+1].append(i+1+portals[i])
    
    que = deque()
    visited = set()
    que.append(1)
    visited.add(1)
    while que:
        cur = que.popleft()
        if cur == dest:
            print('YES')
            return
        for neighbour in graph[cur]:
            if neighbour not in visited:
                visited.add(neighbour)
                que.append(neighbour)
    print('NO')


main()