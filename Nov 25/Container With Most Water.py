class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        l = 0
        r = n - 1 
        while l < r:
            mn = min(height[r], height[l])
            res = max(res , (r - l) * mn)
            if mn == height[l]:
                l += 1
            else:
                r -= 1
        return res