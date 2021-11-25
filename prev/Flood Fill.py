class Solution:
    def floodFill(self, image , sr, sc, newColor):
        
        stack = [[sr,sc]]
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        image[sr][sc] = newColor
        while len(stack) > 0:
            current = stack.pop()
            r = current[0]
            c = current[1]
            if r > 0 and image[r-1][c] == oldColor:
                image[r-1][c] = newColor
                stack.append([r-1,c])
            if r < len(image)-1 and image[r+1][c] == oldColor:
                image[r+1][c] = newColor
                stack.append([r+1,c])
            if c > 0 and image[r][c-1] == oldColor:
                image[r][c-1] = newColor
                stack.append([r,c-1])
            if c < len(image[r])-1 and image[r][c+1] == oldColor:
                image[r][c+1] = newColor
                stack.append([r,c+1])
        return image
arr = [[0,0,0],[0,1,1]]
obj = Solution()
print(obj.floodFill(arr,1,1,1))
                



        