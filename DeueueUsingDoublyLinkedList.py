class Node:
    def __init__(self,item = None,prev=None,next=None):
        self.item = item
        self.prev =prev
        self.next = next
class dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def insert_front(self,data):        
        n = Node(data,None,self.front)
        if self.is_empty():
           
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.item_count+=1
        
    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.front.prev=n
        self.rear=n  
        self.item_count+=1  
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None        
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count_=1   
    def get_front(self):    
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item
    def get_rear(self):    
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
q1=dequeue()    
q1.insert_front(1)
q1.insert_front(2)
q1.insert_front(3)
q1.insert_front(4)
q1.insert_front(5)
q1.insert_front(6)
print(q1.get_front())
print(q1.get_rear())
print("Size",q1.size())

q1.insert_rear(7)
q1.insert_rear(8)
print()
q1.delete_front()
q1.delete_rear()
print(q1.get_front())
print(q1.get_rear())
print("Size",q1.size())
print(q1.item_count)
