# Almost complete binary Tree 
#Heap-|-MaxHeap and MinHeap
class heap:
    def __init__(self):
       self.heap=[]              
    def create_heap(self,list1):
        for i in list1:
            self.insert(i)
    def insert(self,i):
        index=len(self.heap)        
        parent_Index=(index-1)//2
        while index>0 and self.heap[parent_Index]<i:
            if index==len(self.heap):
                self.heap.append(self.heap[parent_Index])   
            else:
                self.heap[index]=self.heap[parent_Index]
            index=parent_Index
            parent_Index=(index-1)//2    
        if index==len(self.heap):
            self.heap.append(i)        
        else:
            self.heap[index]=i
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()   
        return self.heap[0]  
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        left_child_Index=2*index+1
        right_child_Index=2*index+2
        while left_child_Index<len(self.heap):
            if right_child_Index<len(self.heap):
                if self.heap[left_child_Index]>self.heap[right_child_Index]:
                   if self.heap[left_child_Index]>temp:
                       self.heap[index]=self.heap[left_child_Index] 
                       index=left_child_Index
                   else:
                       break
                else:
                    if self.heap[right_child_Index]>temp:
                       self.heap[index]=self.heap[right_child_Index] 
                       index=right_child_Index    
                    else:
                        break
            else:   #if No Right Child
                if self.heap[left_child_Index]>temp:
                    self.heap[index]=self.heap[left_child_Index]
                    index=left_child_Index
                else:
                    break
            left_child_Index=2*index+1
            right_child_Index=2*index+2    
        self.heap[index]=temp
        return max_value  
    def heap_sort(self,list1):
        self.create_heap(list1)
        list2=[] 
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2
class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg=msg
    def __str__(self):
        return msg
            
            
list1=[12,34,22,45,67,87,72,17,90,24,5,19,53] 
h=heap()               
list1=h.heap_sort(list1)

print(list1)