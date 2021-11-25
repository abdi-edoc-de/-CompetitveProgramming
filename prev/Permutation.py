class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in nums:
            arr.append([i])
        ret = []
        for i in arr:
            self.helper(nums,i,ret)
        return ret
            
    def helper(self, nums, pnums, ret):
        temp = []  + pnums
        if len(temp) == len(nums):
            ret.append(temp)
        else:
            for i in nums:
                if i not in temp:
                    print(temp)
                    temp.append(i)
                    self.helper(nums,temp,ret)
                    temp.pop()
                
            
        
