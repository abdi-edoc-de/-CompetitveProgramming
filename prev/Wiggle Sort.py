class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)-1)//2
        low = mid
        high = len(nums) - 1
        arr = []
        while low >= 0 or high > mid:
            
            if low < 0 and high > mid:
                # arr.append(nums[low])
                arr.append(nums[high])
            elif low >= 0 and high <= mid:
                arr.append(nums[low])
            else:
                
                arr.append(nums[low])
                arr.append(nums[high])
            print(f'{nums[low]} {nums[high]}')
            low -=1
            high -=1
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        return nums
            
            
