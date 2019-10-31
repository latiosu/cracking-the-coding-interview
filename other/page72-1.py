# Example: Numbers are randomly generated and stored into an (expanding) array.
# How would you keep track of the median?

import heapq

minHeap = []
maxHeap = []
median = 0

def trackMedian(newNumber):
    # Keep count of how many numbers seen so far
    global median, minHeap, maxHeap
    if len(minHeap) + len(maxHeap) == 0:
        median = newNumber

    # Update min heap (for numbers above median)
    if newNumber > median:
        heapq.heappush(minHeap, newNumber)

    # Update max heap (for numbers below median)
    elif newNumber <= median:
        # Use negatives as there isn't a max heap in Python
        heapq.heappush(maxHeap, -newNumber)

    # Balance heaps to ensure median can be computed from roots
    if len(minHeap) - len(maxHeap) > 1:
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))
    elif len(maxHeap) - len(minHeap) > 1:
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    # Compute median from roots
    if (len(minHeap) + len(maxHeap)) % 2 == 0:
        median = (minHeap[0] - maxHeap[0]) / 2
    else:
        median = -maxHeap[0]

# User stdin for infinite stream of numbers
while True:
    trackMedian(int(input()))
    print("Median: {}".format(median))