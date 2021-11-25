# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        temp = head 
        while temp:
            nodes.append(temp)
            temp = temp.next
        size = len(nodes)        
        ind = size - n
        if size == 1:
            return 
        elif ind == size -1:
            nodes[ind-1].next = None
            return nodes[0]
        elif ind == 0:
            return nodes[0].next
        else:
            nodes[ind-1].next = nodes[ind+1]
            return nodes[0]
            
        
