from typing import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head) :
        if head is None:
            return head
        elif head.next is None:
            return head
        temp = head
        while temp is not None:
            temp1 = temp
            while temp1 is not None:
                if temp1.val < temp.val:
                    i = temp.val
                    temp.val = temp1.val
                    temp1.val = i
                temp1 = temp1.next
            temp= temp.next
        return head



            
                        
            

        


n = ListNode(1)
n.next = ListNode(3)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)
n.next.next.next.next = ListNode(3)
n.next.next.next.next.next = ListNode(3)
obj = Solution()
head= obj.insertionSortList(n)
while head is not None:
    print(head.val)
    head = head.next