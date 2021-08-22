class Solution:
    def intersection(self, nums1 , nums2):

        result = set()
        map = {}
        for i in nums1:
            map[i]=1
        for i in nums2:
            if i in map:
                result.add(i)
        return list(result)
obj=Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(obj.intersection(nums1,nums2))
def str_to_unicode(s: str):
    return s.encode("unicode_escape").decode()
print(str_to_unicode(':joy '))