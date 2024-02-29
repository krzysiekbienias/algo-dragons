class Graph():
    def __init__(self,graph_type:str) -> None:
        self._graph_type=graph_type
        self.adj_list_representation={}
        
    def add_vertex(self,u:(int,str)):
        """add_vertex 

        Description
        -----------
        Method to add an vertex to the graph

        Parameters
        ----------
        u : int,str
        """
        
        if u not in self.adj_list_representation:
            
            self.adj_list_representation[u]=[]
        else:
            print(f'Vertex {u} already exists.')
    
    def remove_vertices(self,u):
        pass
    