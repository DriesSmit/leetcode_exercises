from queue import PriorityQueue

class PriorityQueueWrapper:
    def __init__(self, max_queue=False):
        self.queue = PriorityQueue()
        self.max_queue = max_queue
        self.count = 0  # To track the number of elements in the queue

    def add(self, item):
        # If max_queue is True, insert item with negative priority
        priority = -item if self.max_queue else item
        self.queue.put((priority, item))  # Store (priority, value)
        self.count += 1  # Increment count with each addition

    def pop(self):
        if not self.is_empty():
            self.count -= 1  # Decrement count with each removal
            return self.queue.get()[1]  # Retrieve the actual value
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return self.queue.empty()

    def __len__(self):
        # Override len() to return the size of the queue
        return self.count

# Example usage
# Min Priority Queue
min_pq = PriorityQueueWrapper()
min_pq.add(10)
min_pq.add(1)
min_pq.add(5)

print("Min Priority Queue:")
while not min_pq.is_empty():
    print(min_pq.pop())  # Outputs: 1, 5, 10

# Max Priority Queue
max_pq = PriorityQueueWrapper(max_queue=True)
max_pq.add(10)
max_pq.add(1)
max_pq.add(5)

print("\nMax Priority Queue:")
while not max_pq.is_empty():
    print(max_pq.pop())  # Outputs: 10, 5, 1
