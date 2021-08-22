class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) ==1:
            return s
        elif len(s) == 0:
            return s
        
obj = Solution()
print(obj.reorganizeString("22215"))


        
       
def some(s):
    lst =(s)
    print(lst)

    for i in range(1,len(lst)):
        # print(i)   
        if lst[i] == lst[i-1]:
            # print(i)
            for j in range(i,len(lst)):
                if lst[j]!=lst[i] :
                    lst[i],lst[j]=lst[j],lst[i]
                    break
                if lst[i-1] == lst[i] and j==len(lst)-1:
                    i=0
                    lst[-1],lst[0]=lst[0],lst[-1]
    return s
print(some([1,2,2,1,2]))