from heapq import heapify, heappop,heappush
from typing import DefaultDict
def solve(n,employee,m, applications):
    heapify(applications)
    count = 0
    mn = {}
    while applications:
        cost , em , _ = heappop(applications)
        if em in mn:
            mn[em] = min(cost,mn[em])
        else:
            mn[em] = cost
    ret = 0
    for i in mn:
        count += 1
        ret += mn[i]
    if count == n -1:
        print(ret)
    else:
        print(-1)
    
        
    



def main():
    n= int(input())
    employee = list(map(int,input().split()))
    m = int(input())
    applications = []
    for _ in range(m):
        arr = list(map(int,input().split()))
        arr[0] , arr[2] = arr[2] , arr[0]
        applications.append(arr)
    solve(n, employee, m, applications)
main()
