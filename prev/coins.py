from collections import deque
from typing import DefaultDict


def main():
    lst = []
    for i in range(3):
        lst.append(input())
    indegree = {'A' : 0 , 'B' : 0 , 'C' : 0}
    graph = DefaultDict(list)

    for coins in lst:
        if coins[1] == '>':
            graph[coins[2]].append(coins[0])
            indegree[coins[0]] +=1
        else:
            graph[coins[0]].append(coins[2])
            indegree[coins[2]] +=1
    que = deque()
    for i in indegree:
        if indegree[i] == 0:
            que.append(i)

            break
    if not que:
        print('Impossible')
    
    ret = ''
    while que:
        cur = que.popleft()
        ret += cur
        for i in graph[cur]:
            indegree[i] -=1
            if indegree[i] == 0:
                que.append(i)
    print(ret)

main()