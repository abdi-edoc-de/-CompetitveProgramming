class Solution:
    def largestPerimeter(self, nums):
        if len(nums)<3:
            return 0
        nums = sorted(nums)
        index = len(nums)
        while index >=3:
            possible_tri_nums = nums[index-3:index]            
            if self.can_nums_make_traiangle(possible_tri_nums):
                return self.sum(possible_tri_nums)
            index -=1
        return 0

    def can_nums_make_traiangle(self,arr):
        if arr[0]+arr[1] <= arr[2]:
            return False
        if arr[2]+arr[1] <= arr[0]:
            return False
        if arr[0]+arr[2] <= arr[1]:
            return False
        return True
    def sum(self,arr):
        sum =0
        for i in arr:
            sum +=i
        return sum
            
nums = [3,6,2]
obj = Solution()
print(obj.largestPerimeter(nums))