import heapq
from typing import DefaultDict
def solve(n, k , index, temps):
    heap = []
    ret = [-1] * (n)

    visited = set()
    length = len(index)

    for i in range(length):
        heapq.heappush(heap,(temps[i],index[i]-1))
    val = 0
    while heap:
        cost, cur = heapq.heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        if ret[cur] == -1:
            val += 1
            ret[cur] = cost
        if val == n:
            break
        neihgbours = [cur - 1, cur+1]
        for i in neihgbours:
            if 0 <= i < n and i not in visited :
                heapq.heappush(heap,(cost + 1,i ))
    for i in ret:
        print(i , end= ' ')    
    

def main():
    t = int(input())
    for i in range(t):
       input()
       nk = list(map(int,input().split()))
       n = nk[0]
       k = nk[1]
       index = list(map(int,input().split()))
       temps = list(map(int,input().split()))
       solve(n,k,index,temps)



main()