
from re import match
from typing import DefaultDict, Match


def solve(n, k):
    no_winner = DefaultDict(int)
    matchs = []
    length = n+1
    if n == 1:
        print(-1)
        return
    for i in range(1,length):
        
        for j in range(i+1,length):
            if k > no_winner[i]:
                no_winner[i] +=1
                matchs.append((i,j))
            else:
                no_winner[j] +=1
                matchs.append((j,i))
    # print(no_winner)
    # print(matchs)
    matchs.sort()
    for i in no_winner:
        if no_winner[i] != k:
            print(-1)
            return
    print(len(matchs))
    for i in matchs:
        print(i[0],i[1])


    


def main():
    arr = list(map(int,input().split()))
    solve(arr[0],arr[1])
main()