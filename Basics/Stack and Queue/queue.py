
# Q U E U E


# CONCEPT:
#   A Queue is a linear data structure that follows the
#   FIFO principle — First In, First Out.
#   Think of a line at a ticket counter: first person served first.

# KEY PROPERTIES:
#   - Insertion (enqueue) happens at the REAR.
#   - Deletion  (dequeue) happens at the FRONT.

# TIME COMPLEXITY (using deque):
#   - Enqueue : O(1)
#   - Dequeue : O(1)
#   - Peek    : O(1)
#   - Search  : O(n)

# SPACE COMPLEXITY: O(n)




from collections import deque   # Python's fast, thread-safe double-ended queue


queue = deque()  # Initialize an empty queue

# Enqueue elements
queue.append(1)  # Enqueue 1
queue.append(2)  # Enqueue 2


# Dequeue elements
el1 = queue.popleft()  # Dequeue (removes 1)
el2 = queue.popleft()  # Dequeue (removes 2)
print(el1)  # Output: 1
print(el2)  # Output: 2


# Remove all elements from queue.
queue.clear() 

# Return number of elements in queue. 
size = len(queue) 


