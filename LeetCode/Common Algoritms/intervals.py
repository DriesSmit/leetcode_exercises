# Python Code to Merge Overlapping Intervals by checking 
# overlapping intervals only

def mergeOverlap(arr):
    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])

# Inplace updates
# Python Code to Merge Overlapping Intervals in-place

# Merge overlapping intervals in-place. We return
# modified size of the array arr.
# def mergeOverlap(arr):
    
#     # Sort intervals based on start values
#     arr.sort()

#     # Index of the last merged 
#     resIdx = 0

#     for i in range(1, len(arr)):
        
#         # If current interval overlaps with the 
#         # last merged interval
#         if arr[resIdx][1] >= arr[i][0]:           
#             arr[resIdx][1] = max(arr[resIdx][1], arr[i][1])
        
#         # Move to the next interval
#         else:            
#             resIdx += 1
#             arr[resIdx] = arr[i]

#     # Returns size of the merged intervals
#     return resIdx + 1

# if __name__ == "__main__":
#     arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    
#     # Get the new size of the array after merging
#     newSize = mergeOverlap(arr)

#     # Print the merged intervals based on the new size
#     for i in range(newSize):
#         print(arr[i][0], arr[i][1])
