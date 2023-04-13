graph = {'A':['B', 'C', 'D'], 'B':['E'], 'C':['D', 'E'], 'D':[], 'E':[]}
visited = set()
def dfs(graph,root, visited=None):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

print(dfs(graph, 'A'))