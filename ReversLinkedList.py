# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed = ListNode(head.val)
        temp = head.next;
        while temp is not None:
            temp1 = reversed
            reversed = ListNode(temp.val)
            reversed.next = temp1;
            temp = temp.next     
        while reversed is not None:
            print(reversed.val)
            reversed = reversed.next
        return reversed



        
# si = ListNode(6)
# fi = ListNode(5)
# fo = ListNode(4)
# th = ListNode(3)
tw = ListNode(2)
o = ListNode(1)
# o.next = tw
# tw.next = th
# th.next = fo
# fo.next =fi
# fi.next = si

obj = Solution()
obj.reverseList(o)