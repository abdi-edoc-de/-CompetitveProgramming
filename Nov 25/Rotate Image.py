class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            l = i
            r = n - i -1
            if l != r:
                self.rotat(l, r, matrix)
    def rotat(self, l, n, matrix):
        dir = [self.transfer1, self.transfer2, self.transfer3, self.transfer4]
        r = l
        for i in range(l,n):
            c = i
            temp = matrix[r][c]
            for d in dir:
                # print(temp , r,c)
                temp , matrix[r][c] = matrix[r][c] , temp
                r, c = d(r,c,n,l)
            temp , matrix[r][c] = matrix[r][c] , temp
    def transfer1(self,r,c,n,l):
        return c,n
    def transfer2(self,r,c,n,l):
        return n, n-(r - l)
    def transfer3(self, r, c, n,l):
        return n - (n - c) , l
    def transfer4(self, r, c, n,l):
        return l, (n - r) + l
