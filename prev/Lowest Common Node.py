class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root,p,q: 'TreeNode'):
        current = root 
        stack = []
        arr = []
        check = False
        while True:
            # while current is not None:
            #     stack.append(current)
            #     stack.append(current)
            #     current = current.left
            # if len(stack) == 0:
            #     return
            # current =stack.pop()
            # if len(stack) > 0 and stack[-1] == current:
            #     current = current.right
            # else:
            #     print(current.val)
            #     current = None

            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                # print(current.val)
                if current.val == p:
                    arr = []
                    check = True
                if current.val == q:
                    arr.append(current)
                    break
                if check == True:
                    arr.append(current)
                current = current.right
            else:
                break
        for i in arr:
            print(i.val)
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

obj = Solution()
print(obj.lowestCommonAncestor(bt,2,5))
