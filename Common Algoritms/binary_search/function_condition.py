def binary_search_by_function(lst, target, func):
    """
    Performs binary search on lst using func(x), assuming func(lst) is sorted.
    Returns the index of the element in lst where func(element) == target.
    If not found, returns -1.
    """
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = func(lst[mid])
        if mid_val == target:
            return mid  # Element found at index mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

# Define your list and function
lst = [1, 2, 3, 4, 5]
def double(x):
    return x * 2

# The outputs of double(x) are [2, 4, 6, 8, 10], which are sorted
target = 8

# Perform the binary search
index = binary_search_by_function(lst, target, double)

if index != -1:
    print(f"Element {lst[index]} at index {index} satisfies double({lst[index]}) == {target}")
else:
    print("No element found that satisfies the condition.")
