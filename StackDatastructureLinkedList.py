class Node:
    def __init__(self ,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.top=None
        self.item_count=0
    def is_empty(self):
        return self.top==0
    def push(self,data):
        n=Node(data,self.top)
        self.top =n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.top.item    #data ek variable hai item ko display krne ke liye liya gyahai
            self.top=self.top.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
    def peak(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError("Stack ia empty")
    def size(self):
        return self.item_count    
            
s1=Stack()
s1.push(2)
s1.push(4)
s1.push(6)
s1.push(8)
s1.push(76)
print("Total element in the stack",s1.size())

print("Top element in the stack",s1.peak())
print("poped element is ",s1.pop())
print("Top element in the stack",s1.peak())
print("Top element in the stack",s1.peak())


                   
    