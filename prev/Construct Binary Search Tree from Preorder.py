class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        current = root
        for i in range(1,len(preorder)):
            while True:
                if current.val > preorder[i]:
                    if current.left is None:
                        current.left = TreeNode(preorder[i])
                        current = root
                        break
                    else:
                        current = current.left
                elif current.val < preorder[i]:
                    if current.right is None:
                        current.right = TreeNode(preorder[i])
                        current = root 
                        break
                    else:
                        current = current.right
        return root

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
obj = Solution()
arr = [8]
bt = obj.bstFromPreorder(arr)
preorder(bt)
            