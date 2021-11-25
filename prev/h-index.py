class Solution:
    def hIndex(self, citations):
        citations = sorted(citations)

        if citations == []:
            return 0
        if len(citations) == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0
        ind =1
        print(citations)
        for i in range(len(citations)-1,-1,-1):
            # print(i)
            if citations[i] == ind:
                return ind
            if citations[i] < ind:
                return ind -1
            ind+=1
        return ind-1
        
        
        
                
obj = Solution()
arr= [11,15]
print(obj.hIndex(arr))


# arr = []   
# for i in range(5000):
#     arr.append(i)
# print(arr)