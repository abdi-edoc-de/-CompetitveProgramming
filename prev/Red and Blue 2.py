from heapq import heappop , heappush
from typing import MappingView
def solve(n,reds,m,blues ):
    
    bluePre = blues.copy()
    redPre = reds.copy()
    for i in range(1,m):
        bluePre[i] += bluePre[i-1]
    for i in range(1,n):
        redPre[i] += redPre[i-1]
    print(max(0,(max(0,max(redPre))+max(0,max(bluePre)))))

    
    
    

    




    


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        reds = list(map(int,input().split()))
        m = int(input())
        blues = list(map(int,input().split()))
        solve(n,reds,m,blues)
main()