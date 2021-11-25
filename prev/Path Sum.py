class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root , targetSum: int) -> bool:
        stack = []
        current = root
        sum = 0
        while True:
            if current is not None:
                sum = sum + current.val
                stack.append([current,sum])
                current = current.left
            elif stack:
                lst = stack.pop()
                current = lst[0]
                sum = lst[1]
                print(f'this is current {current.val} sum = {sum}')
                # print(f'this is the sum {sum}')
                if current.left is None and current.right is None and sum == targetSum:
                    return True
                if current.right is None:
                    sum = sum - current.val
                current = current.right
            else:
                break
        return False
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

ot = TreeNode(1)
ot.left = TreeNode(-2)
ot.left.left = TreeNode(1)
ot.left.left.left = TreeNode(-1)
ot.left.right = TreeNode(3)
ot.right= TreeNode(-3)
ot.right.left = TreeNode(-2)

obj = Solution()
print(obj.hasPathSum(ot,-4))