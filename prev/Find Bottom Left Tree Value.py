class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        current = root
        stack = []
        depth = 0
        check = True
        arr = []
        while True:
            if current is not None:
                depth +=1
                stack.append([depth,current, check])
                current = current.left
                check = True
            elif stack:
                lst = stack.pop()
                arr.append(lst)
                depth = lst[0]
                # print(lst[1].val)
                current = lst[1].right
                check = False
            else:
                break
        max = arr[0][0]
        max_nodes = []
        for i in arr:
            if i[0] > max:
                max = i[0]
        for i in arr:
            if max == i[0]:
                max_nodes.append(i)
        for i in max_nodes:
            if i[2] == True:
                return i[1].val
        return max_nodes[0][1].val

            
bt = TreeNode(4)
bt.left= TreeNode(2)
bt.left.left= TreeNode(1)
bt.left.right = TreeNode(3)
bt.right = TreeNode(7)
bt.right.left = TreeNode(5)
bt.right.right = TreeNode(8)

o = TreeNode(1)
o.left = TreeNode(2)
o.left.left = TreeNode(4)

o.right = TreeNode(3)
o.right.left = TreeNode(5)
o.right.left.left = TreeNode(7)
o.right.right = TreeNode(6)

ot = TreeNode(2)
ot.left = TreeNode(1)
ot.right = TreeNode(3)
obj = Solution()
print(obj.findBottomLeftValue(ot))