from collections import defaultdict, deque
from typing import DefaultDict


def solve(reposts):
    graph = DefaultDict(list)
    indegree = defaultdict(int)
    for i in reposts:
        graph[i[2]].append(i[0])
        indegree[i[0]] +=1
    que = deque()
    visited = set()
    visited.add('polycarp')
    que.append((1, 'polycarp'))
    pop = 0
    while que:
        cost , node = que.popleft()
        pop = max(cost,pop)

        for neighbour in graph[node]:
            indegree[neighbour] -=1
            if neighbour not in visited and indegree[neighbour] == 0:
                visited.add(neighbour)
                que.append((cost + 1,neighbour))
    print(pop)
        


def main():
    reposts = []
    t  = int(input())
    for i in range(t):
        st = input()
        st =st.lower()
        
        reposts.append(st.split())
    solve(reposts)
main()
    