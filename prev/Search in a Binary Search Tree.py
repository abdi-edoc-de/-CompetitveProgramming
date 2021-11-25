
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        arr = []
        if root:
            if root.val == val:
                print(f'[root.val == val] {root.val} j')
                return root
            elif root.val > val:
                return self.searchBST(root.left,val)
            else:
                return self.searchBST(root.right ,val)
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
obj = Solution()
print(obj.searchBST(bt , 9))


        