#linked list
#assume all linked list is doubly linked list and unsorted
class LinkedList:
    def __init__(self,headNode):
        self.head = headNode
    def search(self,key):
        cur = self.head
        while cur is not None and cur.key != key:
            cur = cur.nxt
        return cur
    def insert(self,x):
        x.nxt = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
    def delete(self,x):
        if x.prev == None:
            self.head = x.nxt
            self.head.prev = None
        elif x.nxt != None:
            x.prev.nxt = x.nxt
            x.nxt.prev = x.prev
        else:
            x.prev.nxt = None
            x.prev = None
#在链表头尾之间加入一个哑对象作为哨兵，可以显著的简化代码。head.prev = nil
# tail.nxt = nil nil.nxt = head nil.prev = tail

class Node:
    def __init__(self,key,nxt=None,prev=None):
        self.key = key
        self.nxt = nxt
        self.prev = prev

