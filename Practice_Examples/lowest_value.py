
def find_lowest(arr):
    lowest = arr[0] # sys.maxsize
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
    return lowest


if __name__ == "__main__":
    arr = [2, 54, 32, 3, -10]
    print(find_lowest(arr))