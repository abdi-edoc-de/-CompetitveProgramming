from typing import Text


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        cp = p
        cq = q
        stackQ = []
        stackP = []
        while True:
            if cp is not None or cq is not None:
                if cp is None:
                    return False
                if cq is None:
                    return False
                stackP.append(cp)
                stackQ.append(cq)
                cp = cp.left
                cq = cq.left
            elif len(stackP) != 0 and len(stackQ) != 0:
                cq = stackQ.pop()
                cp = stackP.pop()
                if cp.val != cq.val:
                    return False
                cq = cq.right
                cp = cp.right
            else:
                break
        if len(stackP) != len(stackQ):
            return False
        return True


bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

b = TreeNode(1)
b.left = TreeNode(2)

o = TreeNode(1)
o.right = TreeNode(2)

onj = Solution()
print(onj.isSameTree(None,None))