class stack(list):
    def is_empty(self):
        return len(self)==0
    def push_item(self,item):
        self.append(item)
    def pop(self):
        if not self.is_empty():
            return super().pop() #    self ki jgh pr super ka use krte hai list ke pop method chale 
        else:
            raise IndexError("Stack is Empty")
    def peak(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len (self)        
    def insert(self,index,data):
            raise IndexError("No attribute Insert In stack")
s1=stack()        
# s1.insert(0,5)
s1.push_item(12)
s1.push_item(18)
s1.push_item(15)
s1.push_item(13)
print("Top Value is:-",s1.peak())