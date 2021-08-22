class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]        

    def getMin(self) -> int:
        return min(self.stack)
        
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())