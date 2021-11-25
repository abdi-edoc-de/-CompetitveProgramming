from collections import Counter


class Solution:
    def topKFrequent(self, nums, k) :
        count = Counter(nums).most_common()
        print(count)
        arr = []
        for i in range(k):
            arr.append(count[i][0])
        return arr
arr = [1,1,1,2,2,3]
obj = Solution()
print(obj.topKFrequent(arr,2))
        