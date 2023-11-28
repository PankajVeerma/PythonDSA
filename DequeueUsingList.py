class dequeue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
     return len(self.item)==0
    def Insert_front(self,data):      
       self.item.insert(0,data)
    def Insert_rear(self,data):
        self.item.append(data)
    def delete_front(self,data):
        if self.is_empty():    
            raise IndexError("Queue is empty")
        else:
            self.item.pop(0) 
    def delete_rear(self):
        if self.is_empty():    
            raise IndexError("Queue is empty")
        else:
            self.item.pop() 
    def get_front(self):
        if self.is_empty():
            raise IndexError("Qieie is empty")
        else:
            return self.item[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Qieie is empty")
        else:
            return self.item[-1]
    def size(self):
        return len(self.item)        
q1 = dequeue()    
q1.Insert_front(1)
q1.Insert_front(2)
q1.Insert_front(3)
q1.Insert_front(4)
q1.Insert_front(5)
q1.Insert_front(6)
print(q1.get_front())
print(q1.get_rear())
print("Size",q1.size())

q1.Insert_rear(7)
q1.Insert_rear(8)
print()
q1.delete_front(3)
q1.delete_rear()
print(q1.get_front())
print(q1.get_rear())
print("Size",q1.size())
