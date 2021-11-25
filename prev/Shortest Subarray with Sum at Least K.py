from queue import Queue
from collections import deque
class Solution:
    def shortestSubarray(self, nums,k) :
        q = deque()
        sum = 0 
        size = 0
        arr = []
        for i in nums:
            # print('for')
            print(f'i top {i}')
            # print(sum > k)
            if i < k:
                sum += i
                q.append(i)
                size+=1
            elif i >= k:
                return 1
            print(f'sum {sum}')
            if k == sum:
                arr.append(size)
                # sum-=q.get()
                # size-=1
            elif sum > k:
                while sum >= k or q[0]<0:
                    print(f'i {i}')
                    arr.append(size)
                    sum -=q.popleft()
                    size -=1
        print(arr)
        return -1 if len(arr) == 0 else min(arr)
            
            


obj = Solution()
arr = [84,-37,32,40,95]
# [56,-21,56,35,-9]
print(obj.shortestSubarray(arr,167))

