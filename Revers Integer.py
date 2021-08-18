class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed = int(f'-{str(x)[::-1][:-1]}') if x<0 else int(str(x)[::-1])
        print(reversed)
        return reversed if  (-2**31 <= reversed <= 2**31 - 1) else 0

obj = Solution()

print(obj.reverse(2**31))        
        