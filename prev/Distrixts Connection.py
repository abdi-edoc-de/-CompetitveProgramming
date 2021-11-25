from typing import DefaultDict


def districtConnectoin(n,gangs):
    possible_roads = {}
    affilation = DefaultDict(list)
    check = {}

    if len(set(gangs)) == 1:
        print('NO')
    else:
        for i in range(n):
            affilation[gangs[i]].append(i+1)
            temp = set(gangs)
            temp.remove(gangs[i])
            possible_roads[i+1]  =temp
        print('YES')
        for i in possible_roads:
            cur = affilation[possible_roads[i].pop()][0]
            if  i not in check:
                check[i] = cur
                check[cur] = i
                print(i,cur )

def main():
    t = int(input())
    for i in range(t):
        districtConnectoin(int(input()), list(map(int,input().split())))


main()