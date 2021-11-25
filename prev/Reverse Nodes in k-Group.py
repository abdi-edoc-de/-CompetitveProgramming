# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k) :
        temp = head
        arr = []
        while temp is not None:
            arr.append(temp)
            temp = temp.next
        
        n = int(len(arr)/k)
        ind =(k*n)
        left = arr[ind : len(arr)]
        ret = ListNode(0)
        temp = ret
        val = 0
        for i in range(n):
            val +=k
            # print(i)
            for j in range(val-1,val-k-1,-1):
                # print(val)
                temp.next = arr[j]
                temp = temp.next
        temp.next = None
                    
        for i in left:
            temp.next= i
            temp = temp.next
        return ret.next

n = ListNode(1)
n.next = ListNode(3)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)
n.next.next.next.next = ListNode(3)
n.next.next.next.next.next = ListNode(3)
n.next.next.next.next.next.next = ListNode(6)
obj = Solution()
                
head = obj.reverseKGroup(None,4)
while head is not None:
    print(head.val)
    head = head.next
