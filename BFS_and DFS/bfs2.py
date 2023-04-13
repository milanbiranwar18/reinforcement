def bfs(visited, graph, node):  # function for BFS
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }

    visited = []  # List for visited nodes.
    # Driver Code
    print("Following is the Breadth-First Search")
    bfs(visited, graph, '5')  # function calling
