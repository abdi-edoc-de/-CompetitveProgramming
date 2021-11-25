from collections import Counter


class Solution:
    def topKFrequent(self, words, k) :
        words.sort()
        print(words)
        count = Counter(words).most_common()
        print(count)
        arr = []
        for i in range(k):
            arr.append(count[i][0])
        return arr
arr  = ['a','b','c','c']
obj = Solution()
print(obj.topKFrequent(arr,2))