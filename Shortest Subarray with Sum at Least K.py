class Solution:
    def shortestSubarray(self, nums,k) -> int:
        maxIndex = 0
        sum = 0
        for i in range(len(nums)):
            if sum>=k:
                break
            sum +=nums[i]
            maxIndex=i
        # print(maxIndex)
        if sum<k:
            return  -1
        
        summ =0
        lower = maxIndex-1
        for i in range(maxIndex,-1,-1):
            if summ >= k:
                return maxIndex-i
            summ +=nums[i]
            lower-=1
        maxIndex+=1
        return maxIndex


obj = Solution()
print(obj.shortestSubarray([56,-21,56,35,-9],61))
