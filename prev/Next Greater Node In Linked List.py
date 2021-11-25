class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head):
        if head is None:
            return []
        temp= head 
        nodes = []
        while temp is not None:
            nodes.append(temp.val)
            temp = temp.next
        ans = [0] * len(nodes)
        stack =[]
        for i in range(len(nodes)):
            cur = [i,nodes[i]]
            while stack != [] and cur[1] > stack[-1][1]:
                prev = stack.pop()
                ans[prev[0]] = cur[1]
            stack.append(cur)       
        return ans

n = ListNode(2)
n.next = ListNode(1)
n.next.next = ListNode(5)
# n.next.next.next = ListNode(3)
# n.next.next.next.next = ListNode(5)
# n.next.next.next.next.next = ListNode(3)
obj = Solution()
print(obj.nextLargerNodes(n))