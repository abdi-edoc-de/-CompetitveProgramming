from queue import Queue
class MyStack(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.main = Queue()
        self.trans = Queue()
        self.topM = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.main.put(x)     
        self.topM = x  

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        temp = None
        while not self.main.empty():
            temp = self.main.get()
            if not self.main.empty():
                self.trans.put(temp)
        while not self.trans.empty():
            self.topM = self.trans.get()
            self.main.put(self.topM)
        return temp       

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topM

        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.main.empty()
    

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(1))
print(obj.push(2))

print( obj.pop())
print( obj.top())
print( obj.empty())