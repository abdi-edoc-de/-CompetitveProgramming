class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m= len(mat)
        n = len(mat[0])
        
        
        arr = []
        for i in range(m):
            temp = []
            for j in range(n):
                if j != 0:
                    temp.append(mat[i][j] + temp[j-1])
                else:
                    temp.append(mat[i][j])
            arr.append(temp)
        for i in range(m):
            for j in range(n):
                if i != 0:
                    arr[i][j] += arr[i-1][j] 
        for i in range(m):
            for j in range(n):
                r1 = i - k
                r2 = i + k
                c1 = j - k
                c2 = j + k
                if r1 < 0:
                    r1 = 0
                if r2 >= m:
                    r2 = m -1    
                if c1 <0:
                    c1 = 0
                if c2 >= n:
                    c2 = n -1 
            
                
                
                # ret[i][j] = self.prefixSum(arr)
                ans =self.sumRegion(arr,r1,c1,r2,c2)
                mat[i][j] = self.sumRegion(arr,r1,c1,r2,c2)
        return mat
        
    def sumRegion(self,mat, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 != 0:
            return mat[row2][col2] - mat[row2][col1-1]   
        elif row1 != 0 and col1 == 0:
            return mat[row2][col2] - mat[row1-1][col2]
        elif row1 == 0 and col1 == 0:
            return mat[row2][col2] 
        return mat[row2][col2] - mat[row1-1][col2] - mat[row2][col1-1]  + mat[row1-1][col1-1] 

        
