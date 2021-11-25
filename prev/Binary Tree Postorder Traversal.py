class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        arr = []
        current = root
        stack = []
        while True:
            while current is not None:
                stack.append(current)
                stack.append(current)
                current = current.left
            if len(stack) == 0:
                return arr
            current = stack.pop()
            if len(stack) > 0 and stack[-1] == current:
                current = current.right
            else:
                print(current.val)
                arr.append(current.val)
                current = None
        return arr
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

obj = Solution()
print(obj.postorderTraversal(TreeNode(5)))

arr = [1,2]
print(arr[-2:])
# print(arr[-2])
# Im Abdullfeta Dedgeba , forth year software engineering 
# student at Addis Ababa Institute of Technology(AAiT) 
# and Im interested in mobile and backend and 
# problem. 