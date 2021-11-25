from typing import DefaultDict


def solve(names,n):
    graph = DefaultDict(list)
    visited = DefaultDict(int)
    for i in range(n):
        if i != 0:
            cur = names[i]
            prev =names[i-1]
            curl = len(cur)
            prevl= len(prev)
            for j in range(max(curl,prevl)):
                print(cur , prev , 'this')
                if j >= prevl or j >= curl:
                    break
                if cur[j] != prev[j]:
                    graph[prev[j]] = cur[j]
                    visited[prev[j]] += 1
                    visited[cur[j]] += 1
                    break
    print(graph)
    print(visited)
    for i in visited:
        if visited[i] > 2:
            print("Impossible")
            return  
    
    # check = {}
    # delete = set()
    # for i in graph:
    #     if i > graph[i]:
    #         check[graph[i]] = i
    #     else:
    #         delete.add(i)
    # for i in delete:
    #     del graph[i]
    
    # start = ord('a')
    # end = ord('z') +1
    # print(check)
    # print(graph)
    # for i in range(start, end):
    #     char = chr(i)
    #     if char not in check:
    #         if char in graph:
    #             print(char, end='')
    #             print(graph[char], end= '')
    #         else:
    #             print(char,end = '')
        

def main():
    t = int(input())
    names = []
    for _ in range(t):
        names.append(input())
    solve(names,t)
    # print(names)
main()