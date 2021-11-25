# from os import terminal_size


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        arr=[]
        temp =head ;
        i =0;
        while temp is not None and i <=100: 
            arr.append(temp)
            temp = temp.next;
            i+=1;
        print(len(arr))
        t= arr[int(len(arr)/2):len(arr)]
        print(t[0].val)
        print(t[-1].val)

        return temp

    
# si = ListNode(6)
# fi = ListNode(5)
# fo = ListNode(4)
# th = ListNode(3)
# tw = ListNode(2)
o = ListNode(1)
# o.next = tw
# tw.next = th
# th.next = fo
# fo.next =fi
# fi.next = si

obj = Solution()
obj.middleNode(o)