class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head):
        temp= head 
        arr = []
        while temp is not None:
            temp1 = temp
            i = 0
            while temp1 is not None:
                if temp1.val > temp.val:
                    i = temp1.val
                    break
                temp1 = temp1.next
            arr.append(i)
            temp = temp.next
        return arr

n = ListNode(2)
n.next = ListNode(7)
n.next.next = ListNode(4)
n.next.next.next = ListNode(3)
n.next.next.next.next = ListNode(5)
# n.next.next.next.next.next = ListNode(3)
obj = Solution()
print(obj.nextLargerNodes(n))