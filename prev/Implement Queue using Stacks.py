class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = []
        self.tran = []
        self.top = None
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.main) == 0:
            self.top = x
        self.main.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.main) > 0:
            temp = self.main.pop()
            if len(self.main) > 0:
                self.tran.append(temp)
        if len(self.tran) > 0:
            self.top = self.tran[len(self.tran)-1]

        while len(self.tran) > 0:
            self.main.append(self.tran.pop())
        print(self.main)

        return temp
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.main) == 0:
            self.top = None
        return self.top
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.main) == 0
    
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
# param_4 = obj.empty()
# print(param_2)
# print(param_3)
# print(obj.peek())

# print(param_4)