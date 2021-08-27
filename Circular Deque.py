class MyCircularDeque:
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = [0] *k
        self.front = k-1
        self.count = 0
        self.capacity = k
        

    def insertFront(self, value) :
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull() == False:
            self.queue[self.front] = value
            self.count += 1
            self.front -=1
            return True
        return False         

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull() == False:
            self.count +=1
            self.queue.append(value)
            return True
        return False        

    def deleteFront(self) :
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() == False:
            self.front +=1
            self.count -=1
            return True
        return False


        

    def deleteLast(self) :
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() == False:
            self.queue.pop()
            self.count -=1
            return True
        return False
        
        

    def getFront(self) :
        """
        Get the front item from the deque.
        """
        if self.isEmpty() == False:
            return self.queue[self.front+1]
        return -1

        

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty() == False:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity

q = MyCircularDeque(3)

# print(q.insertLast(1))
print(q.insertLast(2))
# print(q.insertFront(3))
# print(q.insertFront(4))
# print(q.getRear())
print(q.isFull())
# print(q.deleteLast())
# print(q.insertFront(4))
# print(q.getFront())

