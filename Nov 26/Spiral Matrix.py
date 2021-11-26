class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        right = n - 1
        left = 0 
        top = 0 
        bottom = m - 1
        ret= []
        while left <= right and top <= bottom:
            if top == bottom:
                ret += matrix[top][left:right+1]
            elif left == right:
                for i in range(top, bottom+1):
                    if i < m:
                        ret.append(matrix[i][left])
            elif left == right and top == bottom:
                ret.append(matrix[top][left])
            else:
                ret += matrix[top][left:right+1]
                for i in range(top+1,bottom):
                    ret.append(matrix[i][right])
                
                ret += matrix[bottom][left:right+1][::-1]
                for i in range(bottom-1,top,-1):
                    ret.append(matrix[i][left])
            left +=1
            right -= 1
            top += 1
            bottom -=1
        return ret