class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # r = 0 
        l = 0 
        indZero = deque()
        n = len(nums)
        numOfOnes = 0
        # tk = k
        
        for r in range(n):
            if nums[r] == 0:
                if k == 0:
                    if indZero:
                        l = indZero.popleft() +1 
                        k += 1
                    else:
                        l = r + 1
                if k!= 0:
                    k -= 1
                    indZero.append(r)
                
            numOfOnes =  max(numOfOnes, r - l + 1)
            
        return numOfOnes
                
                
