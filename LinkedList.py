class Node(object):
    def __init__(self,val):
        self.val=val;
        self.next=None;
class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None;
        self.size = 0;
        self.index = -1;
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        print(self.index)
        if self.index == -1:
            return -1
        if index > self.index:
            return -1
        i=0;
        temp = self.head;
        while i<index:
            temp = temp.next;
            i+=1;
        return temp.val
            


        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val);
        else:
            temp = self.head;
            self.head = Node(val);
            self.head.next = temp;
        self.index +=1;
        self.size +=1;

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val);
        else: 
            temp = self.head;
            while temp.next is not None:
                temp = temp.next;
            temp.next = Node(val);
        self.index +=1;
        self.size +=1;       

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if index == self.size:
            self.addAtTail(val)
            return
        elif index > self.index:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        else:
            temp = self.head;
            i=0;
            while i < index-1:
                temp = temp.next
                i+=1
            added = Node(val)
            added.next = temp.next
            temp.next  =added
        self.size +=1;
        self.index +=1;


            
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if self.index == -1:
            return
        if index > self.index:
            return
        elif index == 0:
            self.head = self.head.next;
        elif index == self.index:
            temp =self.head;
            while temp.next is not None:
                if temp.next.next is None:
                    temp.next = None
                    break;
                temp =temp.next
                
        else:
            temp = self.head;
            i=0;
            while i < index-1:
                temp = temp.next
                i+=1
            temp.next = temp.next.next

        self.index -=1;
        self.size -=1;



    def display(self):
        temp = self.head;
        while temp is not None:
            print(temp.val)
            # print(self.size)
            temp = temp.next;
            


        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtIndex(0,3)
# obj.addAtIndex(0,4)
# obj.addAtIndex(1,1)
obj.addAtHead(5)
obj.addAtIndex(1,2)
obj.addAtHead(6)
obj.addAtTail(2)
# param_1 = obj.get(3)
obj.addAtTail(1)
param_1 = obj.get(5)
obj.addAtHead(2)





# obj.deleteAtIndex(0)
# obj.addAtHead(1)
# obj.deleteAtIndex(0)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.deleteAtIndex(2)
# obj.addAtHead(0)
# obj.addAtIndex(3,4)
# obj.addAtIndex(0,-1)
print(f'get {param_1}')
obj.display()

# ["MyLinkedList","addAtHead","addAtIndex","get","addAtHead","addAtTail","get","addAtTail","get","addAtHead","get","addAtHead"]
# [[],[5],[1,2],[1],[6],[2],[3],[1],[5],[2],[2],[6]]