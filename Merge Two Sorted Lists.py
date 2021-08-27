class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return l1
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        low = l1.val if l1.val < l2.val else l2.val
        map ={}
        for i in range(low,100):
            map[i]=0
        
        for i in range(50):
            if l1 is not None :
                map[l1.val] +=1
                l1 = l1.next
            if l2 is not None:
                map[l2.val] +=1
                l2 = l2.next
            if l1 == None and l2 == None:
                break
        head = ListNode(0)
        temp = head

        for i in map:
            for j in range(map[i]):
                temp.next = ListNode(i)
                temp = temp.next
        return head.next
        
        

obj  = Solution()          
n = ListNode(1)
n.next = ListNode(1)
n.next.next = ListNode(2)
n.next.next.next = ListNode(2)
n.next.next.next.next = ListNode(3)
n.next.next.next.next.next = ListNode(3)
# n.next.next.next.next.next.next = ListNode(3)
s = ListNode(-1)
s.next = ListNode(-1)
s.next.next = ListNode(0)
s.next.next.next = ListNode(12)
s.next.next.next.next = ListNode(13)
s.next.next.next.next.next = ListNode(30)

temp = obj.mergeTwoLists(n,s)
while temp is not None:
    print(temp.val)
    temp = temp.next
