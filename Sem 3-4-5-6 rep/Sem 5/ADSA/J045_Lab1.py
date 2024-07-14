from GraphifyPy import UndirectedGraphs as ug
from GraphifyPy.UndirectedGraphs import UndirectedGraph #Graphify is my own library

graph = UndirectedGraph()
src = 'A' # replace with a vertex of your choice

# add edge using graph.add_edge(vertex1, vertex2)
# add a node using graph.add_node(node_name)

print(ug.bfs(graph_obj=graph, source_node=src)) # returns a path

#function I used for BFS in the library:-

def bfs(graph_obj, source_node=None):

    """
    Performs a breadth-first search on a specified graph. The default parameter for source_node is None which pushes the program to take
    a random call for the source vertex. Else specify the string representing the name of a node.
    
    Parameters
    ----------
    graph_obj: UndirectedGraph object- Graph object on which the depth-first search is performed
        Source node from which the dfs is initialised.

    source_node: default=None; else, the name of the node (dtype = str)

    Raises
    ------
    NodeError
        If specified node is not a part of the graph provided in the parameter.
    """


    if source_node == None:
        from random import randint
        source = graph_obj.nodelist[randint(0, len(graph_obj.connections)-1)]
    elif source_node in graph_obj.connections:
        for node in graph_obj.nodelist:
            if node.name == source_node:
                source = node
    else:
        raise Exception('Node not in nodelist. Try again')

    frontier = []
    frontier.append(source.name)
    traversed = []
    from copy import deepcopy
    while len(frontier)!=0:
        visited = frontier.pop(0)
        traversed.append(visited)
        adj = deepcopy(graph_obj.connections[visited])
        adj.reverse()
        for neighbour in adj:
            if neighbour not in traversed and neighbour not in frontier:
                frontier.append(neighbour)
        
    return traversed