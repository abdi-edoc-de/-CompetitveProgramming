class Solution:
    def hIndex(self, citations):
        citations = sorted(citations)[::-1]
        if citations == []:
            return 0
        if len(citations) == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0
        ind = 0
        l = 0 
        r = len(citations) - 1
        while l <= r:
            mid = l + (r - l)//2
            if citations[mid] >= mid+1:
                ind = mid + 1
                l = mid + 1
            elif citations[mid] < mid + 1:
                r = mid - 1
        return ind
obj = Solution()
arr= [0,0]
print(obj.hIndex(arr))

            