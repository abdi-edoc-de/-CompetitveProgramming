
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}
        for i in range(len(nums)):
            dif = target - nums[i]
            if (dif in map and map[dif] != i):
                return [dif,nums[i]]
            
            map[nums[i]]=i
obj = Solution()


arr =[2,7,11,15]
print(obj.twoSum(arr,9))