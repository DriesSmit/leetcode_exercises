# Find a string
str = "Learn Competitive Programming with GFG!"
first = str.find('m')
last = str.rfind('m')
if first != -1:
    print(f"First Occurrence of m is at index = {first}")
if last != -1:
    print(f"Last Occurrence of m is at index = {last}")

# Reverse a string
str = "Learn Competitive Programming with GFG!"
print(f"Reverse = {str[::-1]}")

# Sort a string
str = "Learn Competitive Programming with GFG!"
str = "".join(sorted(str))
print(f"Sorted string = {str}")


# Reference for better memory/compute management
# Pass by value
def count_space_slow(string, idx):
    if idx == len(string):
        return 0
    return count_space_slow(string, idx + 1) + (string[idx] == ' ')

# Pass by reference (using a list)
def count_space_fast(string, idx):
    if idx == len(string):
        return 0
    return count_space_slow(string, idx + 1) + (string[idx] == ' ')

string = list("Learn Competitive programming with GFG!")
print(count_space_slow(string, 0))
print(count_space_fast(string, 0))