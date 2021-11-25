class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        r = 1
        freq = 0
        temp = 0
        nums.sort()
        while r < len(nums):
            # if r == len(nums) - 1 and k >= 0 :
            #     freq = max(freq, r-l +    1)
            # print(r-l)
            # freq = max(freq, r - l)

            dif = (nums[r] - nums[r - 1]) * (r - l)  
            k = k -dif
            if k < 0 :
                freq = max(freq, r - l)
                k = k + (nums[r] - nums[l])
                l += 1
            r+=1
        freq = max(freq, r - l )

        return freq
                
        
