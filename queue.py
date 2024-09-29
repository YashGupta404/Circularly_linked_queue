class Linked_queue:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self):
            self._element = None
            self._next = None
    def __init__(self):
        self._tail = None
        self._size = 0
        self._head = None
    
    def __len__(self):
        return self._size
    
    def __isEmpty__(self):
        return self._size == 0
    
    def enqueue(self,e):
        newest = self._Node()
        newest._element = e
        if self.__isEmpty__():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._tail._next = self._head 
        self._size +=1
        
    def dequeue(self):
        if self.__isEmpty__():
            print('Queue is Empty')
            
        elif self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            self._head = self._head._next
            self._tail._next = self._head
            self._size -=1
        
            
    def display(self):
        pos = self._head
        while(pos._next != self._head):
            print(pos._element)
            pos=pos._next
        print(pos._element)
        
        
