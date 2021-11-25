# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head 
        size =0
        while temp is not None:
            size +=1
            temp = temp.next
        temp = head
        halfIndex = (size/2) if size % 2 == 0 else int(size/2)+1
        i= 0;
        while i<halfIndex:
            temp = temp.next
            i+=1
        second_half = self.reverseList(temp);
        while second_half is not None:
            if second_half.val != head.val:
                print(False)
                return False
            print(f'{second_half.val} second' )
            second_half = second_half.next
            print(f'{head.val} temp' )
            head = head.next
        print(True)
        return True
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        reversed = ListNode(head.val)
        temp = head.next;
        while temp is not None:
            temp1 = reversed
            reversed = ListNode(temp.val)
            reversed.next = temp1;
            temp = temp.next     
        return reversed
    

# si = ListNode(6)
# fi = ListNode(1)
# fo = ListNode(2)
# th = ListNode(1)
# tw = ListNode(1)
o = ListNode(1)
# o.next = tw
# tw.next = th
# th.next = fo
# fo.next =fi
# fi.next = si

obj = Solution()
obj.isPalindrome(o)