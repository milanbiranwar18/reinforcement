from collections import deque

def bfs(graph, start):
    visited = set()         # Set to keep track of visited nodes
    queue = deque([start])  # Initialize queue with starting node

    while queue:            # Loop until queue is empty
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)

            # Add all neighbors of the current node to the queue
            queue.extend(graph[node] - visited)

    return visited

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

bfs(graph, 'A')   # Output: A B C D E F
