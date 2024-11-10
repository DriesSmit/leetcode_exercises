from collections import defaultdict

# Create a defaultdict with a default value of an empty list
my_dict = defaultdict(int)

# Add elements to the defaultdict
my_dict['fruits'] += 1
my_dict['vegetables'] += 1
my_dict['vegetables'] += 1

# Print the defaultdict
print(my_dict)