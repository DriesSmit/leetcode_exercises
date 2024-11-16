# Example of common set operations in Python

# Initialize two example sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - combines all unique elements from both sets
union_set = set_a | set_b
print("Union:", union_set)

# Intersection - elements that are in both sets
intersection_set = set_a & set_b
print("Intersection:", intersection_set)

# Difference - elements in set_a but not in set_b
difference_set = set_a - set_b
print("Difference (set_a - set_b):", difference_set)

# Symmetric Difference - elements in either set_a or set_b, but not both
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)

# Checking subset - is set_a a subset of set_b?
is_subset = set_a <= set_b
print("Is set_a a subset of set_b?", is_subset)

# Checking superset - is set_a a superset of set_b?
is_superset = set_a >= set_b
print("Is set_a a superset of set_b?", is_superset)

# Adding an element to set_a
set_a.add(9)
print("After adding 9 to set_a:", set_a)

# Removing an element from set_b
set_b.remove(8)
print("After removing 8 from set_b:", set_b)
