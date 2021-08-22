class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        tMap={}
        sMap ={}
        if len(s) != len(t):
            return False
        
        for i in t:
            if i in tMap:
                tMap[i]+=1
            else:
                tMap[i]=1
        for i in s:
            if i in sMap:
                sMap[i]+=1
            else:
                sMap[i]=1
            if i not in tMap:
                return False
        for i in tMap:
            if tMap[i] != sMap[i]:
                return False
        return True 

            

s = "car"
t = "rat"
obj = Solution()
print(obj.isAnagram(s,t))
