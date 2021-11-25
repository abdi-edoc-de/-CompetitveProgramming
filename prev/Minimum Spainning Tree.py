import heapq
class Solution:
    def solve(self, edges, a, b):
        visited = set()
        spaningEdges = set()
        roads = len(edges)
        

        isThere = False
        val = 0
        nodes = set()
        for i in edges:
            nodes.add(i[0])
            nodes.add(i[1])
            if (i[0] == a and i[1] == b) or (i[1] == a and i[0] == b):
                isThere = True
                val = i[2]
        if not isThere:        
            return False 
        edges.sort(key = lambda a:a[2])
        for i in edges:
             
            first = i[0]
            second = i[1]
            cost = i[2]
            # print(len(visited)//2)
            # print(len(nodes))
            if len(visited)//2 == len(nodes) -1 :
                break
            if (first , second) not in visited:
                if isThere and cost == val:
                    print(True)
                    return True
                visited.add((first,second))
                visited.add((second, first))
        print(False)
        return False

edges = [
    [0, 1, 100],
    [0, 2, 100],
    [1, 3, 100],
    [2, 3, 100],
    [1, 2, 100]
]
a = 1
b = 2
edges = [
    [0, 1, 100],
    [1, 2, 100],
    
    ]
]
a = 0
b = 2

Solution().solve(edges,a,b)