#chapter 10
#stack and queue
#stack : LIFO
class Stack:
    def __init__(self):
        self._list = []
        self.top = 0
    def push(self,x):
        self._list.append(x)
        self.top+=1
    def pop(self):
        result = self._list[-1]
        self.top-=1
        del self._list[-1]
        return result
    def stackEmpty(self):
        if self.top == 0:
            return True
        return False
def Queue:
    def __init__(self):
        self._list = []
        self.head = 0
        self.tail = 0
    def enqueue(self,x):
        self._list.append(x)
        self.tail+=1
    def dequeue(self):
        if self.queueEmpty():
            return None
        self.head+=1
        return self._list[self.head-1]
    def queueEmpty(self):
        return True if self.head == self.tail else False
        
