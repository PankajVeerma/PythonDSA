from Singly_Linked_List import *
class Stack( SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().is_empty()#child class se parent class ko  call  
    def push(self ,data):
        self.Insert_Start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.Delete_frist()
            self.item_count-=1
    def peak(self):
        if not self.is_empty():
          return self.start.item
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return self.item_count   
s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
print("Top Element of the stack Till Now",s1.peak())
s1.pop()
s1.push(23)
s1.push(745)
print("Top Element of the stack ",s1.peak())

                       