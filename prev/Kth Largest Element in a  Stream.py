import heapq
class KthLargest:
    
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.heap = self.nums[:self.k]
        heapq.heapify(self.heap)
        for i in range(self.k,len(self.nums)):
            print("som")
            if self.heap[0] < self.nums[i]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,self.nums[i])
            
    def add(self, val):
        if len(self.heap) == 0 :
            heapq.heappush(self.heap, val)
            if self.k == 1 :
                return self.heap[0]
        if self.k > len(self.heap):
            heapq.heappush(self.heap, val)
            return self.heap[0]
        if len(self.heap) >0 and self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]
    

    


arr = [4, 5, 8, 2]
obj = KthLargest(3,arr)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
from collections import Counter
import heapq as h

list1 = [1,2,3,33,3,3]
h.heapify(list1)
h.heappush(list1,55)
print(h.nlargest(3,list1))
print(list1)

# print(list1[:3])