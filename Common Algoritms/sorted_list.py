from sortedcontainers import SortedList

# Create a SortedList
sorted_list = SortedList(key=lambda x: x)

# Add elements
sorted_list.add(10)
sorted_list.add(5)
sorted_list.add(15)
sorted_list.add(2)

# Access the list (it will always be sorted)
print("SortedList after additions:", sorted_list)
# Output: SortedList after additions: [2, 5, 10, 15]

# Add a duplicate element (SortedList allows duplicates by default)
sorted_list.add(5)
print("After adding duplicate 5:", sorted_list)
# Output: After adding duplicate 5: [2, 5, 5, 10, 15]

# Remove an element
sorted_list.remove(10)
print("After removing 10:", sorted_list)
# Output: After removing 10: [2, 5, 5, 15]

# Get the smallest and largest elements
print("Smallest element:", sorted_list[0])  # Output: 2
print("Largest element:", sorted_list[-1])  # Output: 15

# Check if an element exists
print("Does 15 exist?", 15 in sorted_list)  # Output: True
print("Does 10 exist?", 10 in sorted_list)  # Output: False

# Iterate through the elements
for num in sorted_list:
    print("Element:", num)

# Access by index
print("Element at index 1:", sorted_list[1])  # Output: 5




############# ADVANCED EXAMPLE ###############

# List of tuples (e.g., (x, y) coordinates)
points = [(1, 5), (3, 3), (2, 4), (1, 2)]

# Create a SortedList with custom key: sort by x first, then by y
sorted_points = SortedList(points, key=lambda p: (p[0], p[1]))

print("Sorted points after initialization:", sorted_points)
# Output: Sorted points after initialization: [(1, 2), (1, 5), (2, 4), (3, 3)]

# Add a new point
sorted_points.add((1, 3))
print("After adding (1, 3):", sorted_points)
# Output: After adding (1, 3): [(1, 2), (1, 3), (1, 5), (2, 4), (3, 3)]

# Remove a point
sorted_points.remove((2, 4))
print("After removing (2, 4):", sorted_points)
# Output: After removing (2, 4): [(1, 2), (1, 3), (1, 5), (3, 3)]
