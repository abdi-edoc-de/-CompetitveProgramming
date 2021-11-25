# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postOrder(root):
    current = root
    stack = []
    dir = 'left'
    while True:
        while current is not None:
            stack.append(current)
            stack.append(current)
            current = current.left
        if len(stack) == 0:
            break
        current = stack.pop()
        if len(stack) > 0 and stack[-1] == current:
            current = current.right
        else:
            print(current.val)
            current = None
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

postOrder(bt)
def h():
    return ['df',"ssdf","dsf"]
print(h())