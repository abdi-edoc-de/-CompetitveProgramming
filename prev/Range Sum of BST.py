class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        arr = []
        self.helper(root,low,high,arr)
        print(arr)
        return (sum(arr))
    def helper(self, root, low, high, arr):
        if root:
            if (root.val >= low and root.val <=high):
                print(root.val)
                arr.append(root.val)
                self.helper(root.left, low, high, arr)
                self.helper(root.right, low, high, arr)

            elif (root.val < low):
                print(root.val)
                # arr.append(root.val)
                self.helper(root.right, low, high, arr)
            elif (root.val > high):
                self.helper(root.left, low, high, arr)
         
            

        
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)
obj = Solution()
print(obj.rangeSumBST(bt,2,6))

        