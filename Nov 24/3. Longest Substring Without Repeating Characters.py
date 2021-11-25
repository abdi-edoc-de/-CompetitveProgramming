class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        n = len(s)
        l = 0
        long_st = 0
        for r in range(n):
            if s[r] in letters and letters[s[r]] >= l:
                l = letters[s[r]] + 1
                letters[s[r]] = r
            else:
                letters[s[r]] = r
            long_st = max(long_st,((r-l)+1))
        return long_st