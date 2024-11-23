from collections import Counter

# Example list
nums = [1, 2, 2, 3, 3, 3, 4]

# Create a Counter to count the occurrences of each element
counter = Counter(nums)

# Print the Counter object
print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1, 4: 1})

# Access the count of a specific element
print(counter[2])  # Output: 2 (because 2 appears twice)

# Iterate through the Counter
for num, count in counter.items():
    print(f"Number: {num}, Count: {count}")

# Use Counter in a sum calculation
total_occurrences_of_odd_numbers = sum(count for num, count in counter.items() if num % 2 == 1)
print(total_occurrences_of_odd_numbers)  # Output: 4 (1 appears once, 3 appears three times)


print("Output is: " + 3.4)