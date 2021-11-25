from collections import deque
from typing import DefaultDict


def solve(n, employees):
    graph = {}
    indegree = DefaultDict(int)
    visited = [-1] * (n+1)
    for i in range(1,n+1):
        if employees[i-1] != -1:
            graph[i] = employees[i-1]
            indegree[employees[i-1]] +=1 
    que = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            que.append((1,i))
        

    while que:
        cost, node = que.popleft()
        visited[node] = cost
        par = employees[node-1]
        indegree[par] -= 1
        if indegree[par] == 0:
            que.append((cost + 1,par))
    print(max(visited[1:]))


def main():
    t = int(input())
    employees = []
    for _ in range(t):
        employees.append(int(input()))
    solve(t,employees)
main()