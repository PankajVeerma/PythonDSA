from Singly_Linked_List import *
class Stack:
    def __init__(self):
        self.my_list = SinglyLinkedList()
        self.item_count=0
    def is_empty(self):
        self.my_list.is_empty() 
    def push(self,data):
        self.my_list.Insert_Start(data)
        self.item_count+=1
    def pop(self):   
        if not self.is_empty():
            self.mylist.Delete_frist()
            self.item_count-=1
    def peak(self):
         if not self.is_empty():
             return self.my_list.start.item       
    def size(self):
        return self.item_count         
 
  
s = Stack()
s.push(2)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(10)
s.push(32)
print("Top Element",s.peak())