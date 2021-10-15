class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        return self.helper(map,n)
        
    def helper(self,map,n):
        if n in map:
            return map[n]
        elif n == 0:
            val= 1
        elif n == 1:
            val =self.helper(map,n-1)
        elif n >= 2:
            val =self.helper(map,n-1) + self.helper(map,n-2)
        map[n] = val
        return val
