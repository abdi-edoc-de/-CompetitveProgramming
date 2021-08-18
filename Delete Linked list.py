# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                # print(node.val)
                node.val = node.next.val
                node.next = None
            
                break;
            node = node.next
            

four=ListNode(4)
five=ListNode(5)
one=ListNode(1)
nine=ListNode(9)

four.next = five
five.next = one
one.next = nine
 
soul = Solution()
soul.deleteNode(four)
temp = four
while temp is not None:
    print(temp.val)
    temp = temp.next

        