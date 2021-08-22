class Solution:
    def leastInterval(self, tasks ,n):
        if n==0:
            size = len(tasks)
        else:
            size = len(tasks)-1

        re = 0
        for i in range(size):
            if n!=0 and tasks[i] == tasks[i+1]  :
                re+=n
            elif n==0 or tasks[i] != tasks[i+1] :
                re+=1
        return re
        
        
arr = ["A","G","G","A"]          
obj =Solution()
print(obj.leastInterval(arr,0))