class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack = []
        max_num = max(nums)
        ind = nums.index(max_num)
        pre = nums[:ind]
        post = nums[ind+1:]
        root = TreeNode(max_num)
        if pre:
            stack.append([pre, root, True])
        if post:
            stack.append([post, root, False])
        while stack:
            current = stack.pop()
            max_num = max(current[0])
            ind = current[0].index(max_num)
            pre = current[0][:ind]
            post = current[0][ind+1:]
            node = TreeNode(max_num)
            if current[2]:
                current[1].left = node
            else:
                current[1].right = node
            if pre:
                stack.append([pre, node, True])
            if post:
                stack.append([post, node, False])
        return root



        
def inorder(r):
    if r:
        inorder(r.left)
        print(r.val)
        inorder(r.right)
obj = Solution()
arr = [3,6]
bt = obj.constructMaximumBinaryTree(arr)
inorder(bt)
ot = TreeNode(6)
ot.left = TreeNode(3)
ot.left.right = TreeNode(2)
ot.left.right.right = TreeNode(1)
ot.right = TreeNode(5)
ot.right.left = TreeNode(0)

# print('after')
# print(f'''
# {bt.val} 
# {bt.left.val} {bt.left.right.val}  {bt.left.right.right.val}
# {bt.right.val} {bt.right.left.val} 
# ''')
# print(bt.right.val)
# print("other")
# preorder(ot)