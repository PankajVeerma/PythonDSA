class PriorityQueue:
    def __init__(self):
        self.item=[]
    def push(self,data,priority):  #based on small number more priority
       index =0
       while(index<len(self.item)) and self.item[index][1]<=priority:
           index+=1
       self.item.insert(index,(data,priority)) 
    def is_empty(self):
        return len(self.item)==0      
    def pop(self):   # Delete HighestPriority
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.item.pop(0)[0]   
    def size(self):
        return len(self.item)
p=PriorityQueue()        
p.push("Shivani",1)
p.push("Kajal",2)
p.push("pranjli",3)
p.push("Sadhana",5)
p.push("Joya",10)
p.push("Shivam",4)
p.push("Shivanya",7)
p.push("Akanksha",8)
p.push("Shivangi",6)
while not p.is_empty():
    print(p.pop())