

def solve(s):
    n = len(s)  
    count = 0
    l = 0
    for r in range(n):
        if s[r] == 'R':
            l = 0
        else:
            l += 1
        count = max(count, l)
    print(count+1)
def main():
    t = int(input())
    for _ in range(t):
        solve(input())
main()


def calculateScore(word, graph):
    total = 0
    for i in range(1, len(word)):
        total += graph[ (word[i-1], word[i]) ]
    return total


def  dfs(index, k, word, graph):
    nonlocal memo 
    if (index, k, )
    if k <= 0 and index < 0:
        return calculateScore(word, graph)

    maxPos = 0

    for i in range(97, 123):
        word[index] = chr(i)
        curr = dfs(index-1, k-1, word, graph)
        maxPos = max(maxPos, curr)


    return maxPos

def solve2(word, graph, k):
    stack = [ (len(word) - 1, k, ) ]
    visited = set()

    for i,k, j in stack:
        visited[ (i,k,j) ] = calculateScore( word[:i] + ord(j), graph )

    
    






    