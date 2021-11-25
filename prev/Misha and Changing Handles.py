def main():
    n = int(input())
    graph = {}
    for i in range(n):
        old , new = input().split()
        if old in  graph:
            temp = graph[old] 
            graph[temp] = new
            graph[new] = temp
            del graph[old]
        else:
            graph[old] = new
            graph[new] = old
    print(len(graph)//2)
    visited = set()
    for i in graph:
        if i not in visited:
            print(i ,graph[i])
        visited.add(i)
        visited.add(graph[i])
main()