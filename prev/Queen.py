from collections import defaultdict, deque
from typing import DefaultDict


def solve(parrent,respect):
    graph = DefaultDict(list)
    n = len(parrent)

    for k in range(n):
        if parrent[k] != -1:
            graph[parrent[k]].append(k+1)
        else:
            root = k + 1
    
    que = deque()
    que.append(root)
    ret = []
    while que:
        cur = que.popleft()
        
        if graph[cur] == []:
            if respect[cur - 1] == 1:
                ret.append(cur)
        else:
            isRes = True
            
            for child in graph[cur]:
                if respect[child - 1] == 0:
                    isRes = False
                que.append(child)
                if isRes and respect[cur -1 ] == 1:
                    ret.append(cur)
    if ret == []:
        print(-1)
    else:
        ret.sort()
        ans = ''
        for i in range(len(ret)):
            if i != len(ret) - 1: 
                ans += str(ret[i]) + ' '
            else:
                ans += str(ret[i]) 
        print(ans)

    



def main():
    t = int(input())

    parrent = []
    respect = []
    for k in range(0,t ):
        st = input().split()
        parrent.append(int(st[0]))
        respect.append(int(st[1]))
    solve(parrent, respect)
        


main()
