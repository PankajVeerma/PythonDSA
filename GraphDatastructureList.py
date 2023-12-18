class Graph:
    def __init__(self,V_no):
        self.vertex_count=V_no
        self.adj_list = {v: [] for v in range(V_no) }
    def add_edg(self,u,v,weight=1):
        if u>=0<self.vertex_count and v>=0<self.vertex_count:
            self.adj_list[u].append((v,weight)) 
            self.adj_list[v].append((u,weight))
        else:
            print("Invailed Vertex" )     
    def remove_edg(self,u,v):
        if u>=0<self.vertex_count and v>=0<self.vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex!=v] 
           
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list[v] if vertex!=u] 
           
        else:
            print("Invailed Vertex" )     
    def has_edg(self,u,v):
         if u>=0<self.vertex_count and v>=0<self.vertex_count:
            return any(vertex==v for vertex, x in self.adj_list[u])        
         else:
             print("Invailed vertix")   
    def print_adj_list(self):
        for vertex, i in self.adj_list.items():
            print("V",vertex,":",i)  
g = Graph(5)
g.add_edg(0,1)
g.add_edg(1,2)
g.add_edg(1,3)
g.add_edg(2,3)
g.add_edg(3,4)
g.print_adj_list()
                   