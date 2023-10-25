class Node:
    def __init__(self,prev=None,item=None ,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Doubly_Linked_List:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None    
    def Insert_start(self,data):
        n=Node(None,data,self.start)             
        if not self.is_empty():
            self.start.prev=n
        self.start=n   
        
    def Insert_last(self,data,):
        temp=self.start
        if self.start==None:
           while temp.next!=None:
               temp=temp.next
        n =Node(temp,data,None)    
        if temp==None:
            self.start=None
        else:
          temp.next=n  
    def Search(self,data):
        temp=self.start 
        while temp!=None:
            if temp.item==data:
                return temp  
            temp=temp.next    
        return None    
    def Insert_after(self,pos,data):
        if pos is not None:
            n=Node(pos,data,pos.next)
            if pos.next is not None:
                pos.next.prev=n
            pos.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

    def delete_frist(self) :
        if self.start is not None:
            self.start=self.start.next
            # if self.start is not None:
            #     self.start.prev=None
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
       
        else:
            temp=self.start
            while temp is not None:
                    if temp.item==data:
                       if temp.next is not None:
                           temp.next.prev=term,p.prev
                       elif temp.prev is not None:
                           temp.prev.next=temp.next
                       else:
                           self.start=temp.next
                       break    
                    temp=temp.next
    def __iter__(self):
       return Doubly_Linked_List_iterator(self.start) 
# using Itreter

class Doubly_Linked_List_iterator:
    def __init__(self,start):
        self.current =start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
           raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

mylist=Doubly_Linked_List()
mylist.Insert_start(10)
mylist.Insert_last(20)


mylist.Insert_after(mylist.Search(10),15)
mylist.delete_frist()
for i in mylist:
    print(i,end="")