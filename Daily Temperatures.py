class Solution:
    def dailyTemperatures(self, temperatures):
        i=0
        j=0
        ind=0
        arr = []
        while i<len(temperatures):
            ind = 0
            j =i
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    ind = j-i
                    break
                j+=1
            arr.append(ind)
            i+=1
        return arr 
        
obj = Solution()
print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(eval('(3+3)/2'))