class Solution:
    def lastStoneWeight(self, stones):            
        while len(stones) > 1:
            stones = sorted(stones)[::-1]
            first = stones[0]
            second = stones[1]
            if first == second:
                stones = stones[2:]
            elif first != second:
                stones = stones[1:]
                stones[0] = first - second
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
# print([1,3,4][2:])
stones = [11,2,4,1] 
obj = Solution()
print(obj.lastStoneWeight(stones))
d = [34,5]
h = set(d)
h.remove(5)
print(h)
h = set(d)
print(h)