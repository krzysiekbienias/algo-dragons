from introduction import Graph

d1={0:[3],
    1:[0,2,4],
    2:[4],
    3:[5,1],
    4:[5],
    5:[]}

def _dfs(graph:(Graph,dict),vertex:int,visited:set):
    if isinstance(graph,Graph):
        print(vertex)
        visited.add(vertex)
        for neighbor in graph.adj_list_representation[vertex]:
            if neighbor not in visited:
                _dfs(graph,neighbor,visited)
    else:
        print(vertex)
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                _dfs(graph,neighbor,visited)
        
            
def dfs(graph:Graph,vertex:int):
    
    visited=set()
    for vertex in graph:
        if vertex not in visited:
            _dfs(graph,vertex,visited)
    
dfs(graph=d1,vertex=0)