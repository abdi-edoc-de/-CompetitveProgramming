# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head) :
        if head is None:
            return head
        temp = head

        while temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
    

n = ListNode(1)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)
n.next.next.next.next = ListNode(3)
n.next.next.next.next.next = ListNode(3)
# n.next.next.next.next.next.next = ListNode(3)

obj = Solution()
temp = obj.deleteDuplicates(None)
while temp is not None:
    print(temp.val)
    temp = temp.next
