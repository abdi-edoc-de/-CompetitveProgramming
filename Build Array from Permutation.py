class Solution:
    def buildArray(self, nums):
        arr = []
        i =0;
        for i in range(len(nums)):
            arr.append( nums[nums[i]])
        return arr
obj = Solution()
print(obj.buildArray([0,2,1,5,3,4]))





        