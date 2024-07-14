graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited=[] #Think of this as a stack.
def dfs(visited,graph,node):
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("Following is the Depth First Search")
dfs(visited,graph,'5')