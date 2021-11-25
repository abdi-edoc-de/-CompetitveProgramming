# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        temp = head 
        while temp:
            nodes.append(temp)
            temp = temp.next
        n = len(nodes)
        l = 0
        r = n-1
        prev = None
        while l <= r:
            if l == r:
                if prev:
                    prev.next = nodes[l]
                prev = nodes[l]
            else:
                if prev:
                    prev.next = nodes[l]                   
                prev = nodes[r]
                nodes[l].next = prev

            l += 1
            r -= 1
        prev.next = None
                    