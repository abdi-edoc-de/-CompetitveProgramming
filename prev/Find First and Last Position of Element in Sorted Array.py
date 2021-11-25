class Solution:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        ret_l = -1
        ret_r = -1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                ret_l = mid
                print(mid)
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ret_r = ret_l
        l = 0
        r = len(nums) - 1
        while l <= r :
            mid = l + (r - l)//2
            if nums[mid] == target:
                ret_r = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        return [ret_l,ret_r]
            

        
obj = Solution()
arr = [8]
print(obj.searchRange(arr,8))

            

        