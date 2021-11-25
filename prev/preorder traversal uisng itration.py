class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorder(r):
    c = r
    stack = []
    
    while True:
        
        if c is not None:
            stack.append(c)
            c = c.left
        elif(len(stack) != 0):
            c = stack.pop()
            print(c.val)
            c = c.right
        else:
            break
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)
preorder(bt)

            