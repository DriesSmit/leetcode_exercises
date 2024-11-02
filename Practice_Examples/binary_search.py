def binary_search(arr, val):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1
        

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")