# Definition for a binary tree node.
from typing import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        
        current = root
        stack = []
        while True:
            if current.val > val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            if current.val < val:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
        return root
def  inorder(r):
    if r:
        inorder(r.left)
        print(r.val) 

        inorder(r.right)
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

obj = Solution()

ot = obj.insertIntoBST(bt,6)
inorder(ot)

        