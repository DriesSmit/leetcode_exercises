import heapq

# Create a list and heapify it
min_heap = [10, 5, 3, 2, 7]
heapq.heapify(min_heap)  # Transform the list into a min-heap

# Adding elements to the min-heap
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 8)

print("Min-Heap:", min_heap)  # Outputs: [1, 2, 3, 10, 7, 5, 8]

# Removing elements from the min-heap
print("Popped:", heapq.heappop(min_heap))  # Outputs: 1 (smallest element)
print("Min-Heap after pop:", min_heap)     # Outputs the heap with 1 removed

# Heap pushpop
 # If the current number is larger than the smallest in the heap, replace it
# if num > min_heap[0]:
#     heapq.heappushpop(min_heap, num)

# On LeetCode you can just use heappop