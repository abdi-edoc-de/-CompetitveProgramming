import math
class Solution:
    def smallestDivisor(self, nums, threshold) -> int:
        l = 1
        r = max(nums)
        posibleDivs = []
        while l <= r:
            mid = l + (r - l)//2
            if self.sum_of_divided_nums(nums,mid) <= threshold:
                posibleDivs.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        return min(posibleDivs)
            
        
    def sum_of_divided_nums(self,nums , den):
        sum = 0
        for i in nums:
            sum += math.ceil(i/den)
        return sum
    
arr = [2,3,5,7,11]
obj = Solution()
print(obj.smallestDivisor(arr, 11))