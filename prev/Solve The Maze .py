import sys
sys.setrecursionlimit(5000)
def valid(r,c,n,m):
    return 0 <= r < n and 0 <= c < m
def solve(n,m,mat):
    no_g = 0
    dir = [(-1,0),(0,-1),(1,0),(0,1)]
    # print(n,m)
    # print(mat)
    # print(mat[n-1][m-1])
    # return
    for r in range(n):
        for c in range(m):
            if mat[r][c] == "B":
                for d in dir:
                    nr = r + d[0]
                    nc = c + d[1]
                    if  valid(nr,nc,n,m):
                        nei = mat[nr][nc]
                        if  nei == 'G':
                            print('NO')
                            return
                        if nei == '.':
                            mat[nr][nc] = '#'
            if mat[r][c] == 'G':
                no_g += 1
    if no_g > 0 and mat[n-1][m-1] == '#':
        print('NO')
        return
    if mat[n-1][m-1] == 'B':
        print('NO')
        return
    ret = [no_g]
    dfs(ret,mat,n,m,n-1,m-1)
    if ret[0] == 0:
        print('YES')
    else:
        print('NO')
def dfs(ret,mat,n,m,r,c):
    dir = [(-1,0),(0,-1),(1,0),(0,1)]
    if mat[r][c] == 'G':
        ret[0] -= 1
    mat[r][c] = "#"
    for d in dir:
        nr = r + d[0]
        nc = c + d[1]
        if valid(nr,nc,n,m) and mat[nr][nc] != 'B' and mat[nr][nc] != '#':
            dfs(ret,mat,n,m,nr,nc)
            
        
    
def main():
    t = int(input())
    for _ in range(t):
        n,m = list(map(int,input().split()))
        mat = []
        for _ in range(n):
            mat.append([char for char in input()])
        solve(n,m , mat)
main()