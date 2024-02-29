class Graph():
    def __init__(self,graph_type:str) -> None:
        self._graph_type=graph_type
        self.adj_list_representation={}
        
    def add_vertex(self,u:(int,str))->dict:
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
    
    def remove_vertex(self,u:(int,str))->dict:
        """remove_vertex

        Description
        -----------
        Methods to remove a vertex. Please not that we do not remove only a vertex but also all 
        we need to remove vertex from being a neighbor of all other vertices. 
        Parameters
        ----------
        u : int,str
            _description_

        Returns
        -------
        dict
        """
        if u in self.adj_list_representation:
            del self.adj_list_representation[u]
            for v in self.adj_list_representation:
                if u in self.adj_list_representation[v]:
                    v.remove(u)
        
        
        
    