class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        map = {}
        islandNo = 0
        m = len(grid)
        n = len(grid[0])
        stack = []
        
        for i in range(m):
            for k in range(n):
                st = f'{i}{k}'
                if grid[i][k] == 1 and st not in map:
                    islandNo +=1
                    stack.append([i,k])
                while stack:
                    cur = stack.pop()
                    r = cur[0]
                    c = cur[1]
                    curSt = f'{r}{c}'
                    if r == 0 and c ==0 :
                        if grid[r+1][c] == 1:
                            stack.append([r+1,c])
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                        map[curSt] = cur
                    elif r == 0 and c < n-1:
                        if grid[r+1][c] == 1:
                            stack.append([r+1,c])
                        if grid[r][c-1] == 1 :
                            stack.append([r,c-1])
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                    elif r > 0 and r < m-1 and c == 0:
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                        if grid[r-1][c] == 1:
                            stack.append([r-1,c])
                        if grid[r+1][c] == 1:
                            stack.append(r+1,c)
                    elif c == n -1 and r == 0:
                        if grid[r][c-1] == 1:
                            stack.append([r,c-1])
                        if grid[r+1][c] == 1:
                            stack.append([r+1,c])
                    elif r == m-1 and c == 0:
                        if grid[r-1][c] == 1 :
                            stack.append([r-1,c])
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                    elif r == m -1  and c > 0:
                        if grid[r][c-1] == 1:
                            stack.append([r,c-1])
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                        if grid[r-1][c] == 1:
                            stack.append([r-1,c])
                    elif c == n- 1 and r > 0:
                        if grid[r][c-1] == 1:
                            stack.append([r,c-1])
                        if grid[r-1][c] == 1:
                            stack.append([r-1,c])
                        if grid[r+1][c] == 1:
                            stack.append([r+1,c])
                    elif c == n-1 and r == m -1 :
                        if grid[r-1][c] == 1:
                            stack.append([r-1,c])
                        if grid[r][c-1] == 1:
                            stack.append([r,c-1])
                    else:
                        if grid[r][c-1] == 1:
                            stack.append([r,c-1])
                        if grid[r][c+1] == 1:
                            stack.append([r,c+1])
                        if grid[r-1][c] == 1:
                            stack.append([r-1,c])
                        if grid[r+1][c] == 1:
                            stack.append([r+1,c])
                    
                            

        return islandNo
    