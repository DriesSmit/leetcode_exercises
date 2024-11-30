import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    # Distances dictionary initialized to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # Skip processing if we found a shorter way
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update shortest path if found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example Usage:
# Graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Start node
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Output shortest paths
for node, distance in shortest_paths.items():
    print(f"Shortest distance from {start_node} to {node} is {distance}")
