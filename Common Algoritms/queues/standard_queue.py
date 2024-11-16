from collections import deque
"""
Link: https://www.geeksforgeeks.org/queue-in-python/
Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module: 

maxsize - Number of items allowed in the queue.
empty() - Return True if the queue is empty, False otherwise.
full() - Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() - Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() - Return an item if one is immediately available, else raise QueueEmpty.
put(item) - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() - Return the number of items in the queue.
"""

q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue's first element")
print(q[0])
