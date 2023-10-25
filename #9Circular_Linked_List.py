class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Circular_Linked_List:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def Insert_start(self,data):
        n = Node(data )
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next

    def Insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if self.is_empty():
            return None

        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None

    def Insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    def Print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not is_empty():
            if self.last.next == self.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
    def dalete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                     temp=temp.next
                temp.next=self.last.next   
                self.last=temp  
    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.lastitem==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:  
                    temp=self.last.next
                    while temp!=self.last:  
                        if temp.next==self.last :
                            if self.last.item==data:
                                
                              self.delete_last()
                              break           
                        if temp.next.item==data:
                           temp.next=temp.next.next    
                        break
                    temp=temp.next
        #iteration ke liye            
    def __iter__(self):
        if self.last==None:
           return Circular_Linked_List(None)   
        else:
            return Circular_Linked_List_iterator(self.last.next)
    
            # iterator se 
class Circular_Linked_List_iterator:        
    def __init__(self,start):
        self.current=start 
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        
        return data

C_L_L=Circular_Linked_List()
C_L_L.Insert_start(5)
C_L_L.Insert_last(10)
C_L_L.Insert_last(15)
C_L_L.Insert_last(19)
C_L_L.Insert_after(C_L_L.search(15),17)
for i in C_L_L:
    print(i,end=" ")
print()    
C_L_L.Print_list()
                    