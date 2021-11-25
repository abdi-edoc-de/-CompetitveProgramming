# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = None
        second = None
        ind = 0
        temp = head
        while temp:
            if ind == k-1:
                first = temp
            temp = temp.next
            ind += 1
        temp = head
        i = 0
        while i <= ind - k:
            second = temp
            temp = temp.next
            i += 1
        first.val ,second.val = second.val, first.val
        return head