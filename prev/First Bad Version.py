class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        l = 0
        r = n
        while l <= r:
            mid = l + (r - l)//2
            print(mid)
            print(self.isBadVersion(mid))
            if self.isBadVersion(mid):
                ans.append(mid)
                r = mid -1
                # l = 0
            else:
                l = mid + 1
        print(ans)
        return -1 if ans == [] else min(ans)
    def isBadVersion(self, n):
        return n >= 0
obj=Solution()
print(obj.firstBadVersion(4))
