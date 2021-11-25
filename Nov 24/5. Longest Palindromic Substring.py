class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindroms = []
        s = list(s)
        n = len(s)
        
        for i in range(n):
            self.getPalindrom(s,i,i,palindroms)
            if i != n-1 and s[i] == s[i+1]:
                self.getPalindrom(s,i,i+1,palindroms)
        palindroms.sort()
        return ''.join(palindroms[-1][1:])
    def getPalindrom(self,s ,l,r,palindroms):
        while self.isPalindrom(s,r,l): 
            l -= 1
            r += 1
        palindroms.append([r-l-1]+ s[l+1:r])
    def isPalindrom(self,s, r,l):
        n = len(s)
        return 0 <= l < n and 0 <= r < n and s[r] == s[l]