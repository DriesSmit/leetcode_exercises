# https://www.geeksforgeeks.org/eulerian-path-and-circuit/
# https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
# https://www.youtube.com/watch?v=8MpoO2zA2l4
from collections import defaultdict

def find_eulerian_circuit(graph):
    # Prepare a stack and a list to store the circuit
    stack = []
    circuit = []

    # Convert graph to adjacency list for modification
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    # Start with any vertex that has edges (here vertex 0)
    current = list(adj_list.keys())[0]
    stack.append(current)

    while stack:
        if adj_list[current]:
            # If the current vertex has edges, push to stack and follow one edge
            stack.append(current)
            next_vertex = adj_list[current].pop()
            current = next_vertex
        else:
            # Backtrack and add to circuit
            circuit.append(current)
            current = stack.pop()

    # The circuit is built in reverse order, so reverse it
    return circuit[::-1]

# Example usage
graph = [
    (0, 1), (1, 2), (2, 0), (0, 3), (3, 0)
]
circuit = find_eulerian_circuit(graph)
print("Eulerian Circuit:", circuit)
