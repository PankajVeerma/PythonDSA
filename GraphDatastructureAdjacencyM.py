#Adjacency Matrix of Graph
class Graph:
    def __init__(self,V_no):
        self.vertex_count=V_no
        self.adj_matrix = [[0]*V_no for i in range(V_no)]    
    def add_edg(self,u,v,weight=1):
        if u>=0<self.vertex_count and v>=0<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invailed Vertex" )    
    def remove_edg(self,u,v)  :
        if u>=0<self.vertex_count and v>=0<self.sertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invailed Vertex" )            
    def has_edg(self,u,v):
        if u>=0<self.vertex_count and v>=0<self.sertex_count:
            return  self.adj_matrix[u][v] != 0        
        else:
            print("Invailed Vertex" )
    def print_adj_matrix(self):
        for i in self.adj_matrix:
            print(" ".join(map(str,i)) )       
g = Graph(5)
g.add_edg(0,1)
g.add_edg(1,2)
g.add_edg(1,3)
g.add_edg(2,3)
g.add_edg(3,4)
g.print_adj_matrix()