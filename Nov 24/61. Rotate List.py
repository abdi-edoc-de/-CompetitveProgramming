# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        if not head:
            return
        while temp:
            nodes.append(temp)
            temp = temp.next
        n = len(nodes)
        rotates = k // n
        rotates = k - (n * rotates)
        if rotates == 0:
            return head
        ind = (n - rotates) -1
        nodes[ind].next = None
        nodes[-1].next = nodes[0]
        return nodes[ind+1]