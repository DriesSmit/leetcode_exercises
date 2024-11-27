# https://www.topcoder.com/thrive/articles/Line%20Sweep%20Algorithms
from typing import List
import heapq
from sortedcontainers import SortedList

class Event:
    def __init__(self, x, rect):
        self.x = x  # x-coordinate (start or end of rectangle)
        self.rect = rect  # The rectangle associated with this event

    def __lt__(self, other):
        # Events are sorted by x-coordinate, breaking ties with the rectangle's lower y-coordinate
        if self.x != other.x:
            return self.x < other.x
        return self.rect[0] < other.rect[0]

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        events = []
        y_min = float('inf')
        y_max = float('-inf')

        for rect in rectangles:
            events.append(Event(rect[0], rect))  # Start event at x1
            events.append(Event(rect[2], rect))  # End event at x2
            y_min = min(y_min, rect[1])  # Update global y_min
            y_max = max(y_max, rect[3])  # Update global y_max

        # Min-heap to process events in sorted order
        heapq.heapify(events)
        
        # Active y-intervals tracked in a sorted manner
        intervals = SortedList(key=lambda r: (r[1], r[3]))
        y_range = 0

        while events:
            x = events[0].x  # Current x-coordinate
            while events and events[0].x == x:
                event = heapq.heappop(events)
                rect = event.rect
                if x == rect[2]:  # End event
                    intervals.remove(rect)
                    y_range -= rect[3] - rect[1]
                else:  # Start event
                    if any(not (r[3] <= rect[1] or r[1] >= rect[3]) for r in intervals):
                        return False
                    intervals.add(rect)
                    y_range += rect[3] - rect[1]

            # Validate full y-range coverage at this x-coordinate
            if events and y_range != y_max - y_min:
                return False
        return True
    
