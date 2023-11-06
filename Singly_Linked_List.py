class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SinglyLinkedList:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def Insert_Start(self, data ):
        n=Node(data,self.start)  
        self.start=n  
    def Insert_End(self,data,):
        n=Node(data)
        if not self.is_empty():
            temp=self.start 
            while temp.next is not None:      
                temp=temp.next
            temp.next=n    
        else:
            self.start=n    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next    
        return None    
    def insert_after(self,pos, data):
        if pos is not None:
            data=Node(data,pos.next)     # postion diyagya hai(Node ka refrence pass kiya gya hai)
            pos.next=data
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def Delete_frist(self):
        if self.start is not None:
            self.start=self.start.next
    def Delete_End(self):
        if self.start is None :
             pass                       
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None    
    def Delete_Item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None         
        else:
            temp=self.start  
            if temp.item==data:
                self.start= temp.next
            else:
                 while temp.next is not None:         
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return Singly_linked_list_Itretar(self.start)               
                    
                    
                    
                    
                    
#Builten Class itreble nhi hota hai
#class ko itreble bane ke liye
class Singly_linked_list_Itretar:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data    
        
mylist=SinglyLinkedList()      
mylist.Insert_Start(10) 
mylist.insert_after(mylist.search(10),15)
mylist.Insert_End(20)
mylist.Insert_End(30)
mylist.Insert_End(40)
mylist.print_list()
print()

mylist.Delete_frist()
mylist.print_list()
print()

mylist.Delete_End()
mylist.print_list()
print()
mylist.Delete_Item(20)
print()
mylist.print_list()


# using Itretar
for x in mylist:
    print(x,end=" ")
print()