from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.parent = defaultdict(lambda: None)

    def find(self, x):
        if self.parent[x] is None:
            self.parent[x] = x
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.parent[rootY] = rootX

    def count_sets(self):
        # Use a set to collect all unique roots
        unique_roots = {self.find(x) for x in self.parent}
        return len(unique_roots)

# Create a disjoint set
ds = DisjointSet()

# Union some pairs
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)

# Get the number of disjoint sets
print(ds.count_sets())  # Output should be 2, as there are two sets: {1, 2, 3} and {4, 5}
