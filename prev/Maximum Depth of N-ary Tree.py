
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        map = {}
        stack.append(root)
        m = 1
        arr = []
        while len(stack) > 0:
            current = stack.pop()
            print(f'{m} val {current.val}')
            # if current.children == []:
            arr.append(m)            
            if current.children != []:
                if len(current.children) > 1:
                    stack.append(current)
                    m-=1
                stack.append(current.children.pop())
                m+=1


        print(arr)
        return max(arr)

root = Node(1)
root.children = [
    Node(1,[Node(5,[Node(9)]),Node(6)]),
    Node(2),

    Node(4)
]
obj = Solution()
print(obj.maxDepth(root))