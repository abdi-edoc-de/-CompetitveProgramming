import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        arr = []
        for i in lists:
            temp = i
            while temp is not None:
                heapq.heappush(arr,temp.val)
                temp = temp.next
        ret = []

        while len(arr) != 0:
            ret.append(heapq.heappop(arr))
        return ret

