#Stack Datastructure Using Linked LIst
class Stack:
    def __init__(self):
        self.item=[]
    
    def is_empty(self):
        return len(self.item)==0
    def push_item(self,data):
        self.item.append(data)
        print(self.item)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")
    def peak(self):
        if not self.is_empty()        :
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.item) 
s1=Stack()    
s1.push_item(2)
s1.push_item(23)
s1.push_item(63)
s1.push_item(53)
s1.push_item(34)

print(s1.peak())
print(s1.pop())

print()