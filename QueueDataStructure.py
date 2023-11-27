class Queue:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item)==0    
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError("Queue is Empty") 
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Queue is Empty")   
            
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Queue is Empty") 
    def size(self):
        return len(self.item)
q1 = Queue()     
# try:
#     print(q1.get_front())            
# except IndentationError:
#     print(e.arg[0])

q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
try:
    print(q1.get_front())            
except IndentationError:
    print(e.arg[0])
try:
    print(q1.get_rear())            
except IndentationError:
    print(e.arg[0])
try:
   q1.dequeue()      
   print("Length",q1.size())     
except IndentationError:
    print(e.arg[0])