
#                           QUEUE — THEORY & CONCEPTS


# 1. WHAT IS A QUEUE?
#
# A Queue is a linear data structure that follows the FIFO principle:
#                "FIRST IN, FIRST OUT" (or LILO: Last In, Last Out)
#
# The element that is inserted FIRST is the FIRST one to be removed.
# Elements are added at one end called the REAR (or TAIL / BACK)
# and removed from the opposite end called the FRONT (or HEAD).
#
# Real-World Analogies:
#   - A line of people at a ticket counter: First person in line gets served first.
#   - A printer queue: First document sent to print is printed first.
#   - Customer support call waiting line: Callers served in order of arrival.
#   - Operating system CPU scheduling / process queues.
#   - Web server request queues (handling incoming HTTP requests).
#
# Visual Representation:
#
#               ENQUEUE (Insert)
#                     │
#                     ▼
#      ┌───────────────────────────────┐
#      │ REAR                     FRONT│
#      ├───────┬───────┬───────┬───────┤
#  ──► │  40   │  30   │  20   │  10   │ ──► DEQUEUE (Remove)
#      ├───────┴───────┴───────┴───────┤
#      │ (Newest)             (Oldest) │
#      └───────────────────────────────┘
#


# 2. KEY TERMINOLOGY
#
#   FRONT / HEAD  → The exit point; references the oldest element to be removed.
#   REAR / TAIL   → The entry point; references the latest inserted element.
#   ENQUEUE       → Operation to insert an element at the REAR of the queue.
#   DEQUEUE       → Operation to remove and return the element at the FRONT.
#   PEEK / FRONT  → Viewing the front element WITHOUT removing it.
#   ISEMPTY       → Checking whether the queue currently holds zero elements.
#   ISFULL        → Checking whether a fixed-capacity queue is full.
#   SIZE          → Total count of elements currently present in the queue.
#   OVERFLOW      → Error state: attempting to ENQUEUE into an already FULL queue.
#   UNDERFLOW     → Error state: attempting to DEQUEUE or PEEK an EMPTY queue.


# 3. CORE OPERATIONS & TIME COMPLEXITIES
#
#  Operation       Time Complexity     Space Complexity    Description
#  ────────────────────────────────────────────────────────────────────────────
#  Enqueue         O(1)                O(1)                Insert item at REAR
#  Dequeue         O(1)*               O(1)                Remove item at FRONT
#  Peek / Front    O(1)                O(1)                Inspect FRONT item
#  isEmpty         O(1)                O(1)                Check if size == 0
#  isFull          O(1)                O(1)                Check if size == capacity
#  Size            O(1)                O(1)                Get count of elements
#  Search          O(n)                O(1)                Search for an item
#  Access (by idx) O(n)                O(1)                Restricted in pure queue
#  ────────────────────────────────────────────────────────────────────────────
#  Overall Space:  O(n) to store n elements.
#
#  * Important Note on Python:
#    - Using Python `list`: `pop(0)` takes O(n) time because all elements shift!
#    - Using `collections.deque`: `popleft()` takes O(1) guaranteed time.
#    - Using a Linked List with head and tail: Dequeue takes O(1) time.


# 4. OPERATIONS — HOW THEY WORK (STEP BY STEP)
#
#  ── ENQUEUE (Insert at REAR) ──
#  Queue capacity: 4 (initially holding [10, 20])
#
#    Step 1: Check for Queue Overflow (if isFull()).
#    Step 2: Advance the REAR pointer.
#    Step 3: Place new item at REAR.
#
#    Before:            Enqueue(30):            After:
#    FRONT       REAR   FRONT            REAR   FRONT            REAR
#      │           │      │                │      │                │
#      ▼           ▼      ▼                ▼      ▼                ▼
#    [ 10  │  20  │ - ]  [ 10  │  20  │  30  ]  [ 10  │  20  │  30  │  - ]
#
#  ── DEQUEUE (Remove from FRONT) ──
#
#    Step 1: Check for Queue Underflow (if isEmpty()).
#    Step 2: Read value at FRONT.
#    Step 3: Advance FRONT pointer (or remove front node in linked list).
#    Step 4: Return value.
#
#    Before:                    Dequeue() returns 10:   After:
#    FRONT            REAR                              FRONT       REAR
#      │                │                                 │           │
#      ▼                ▼                                 ▼           ▼
#    [ 10  │  20  │  30  ]       10 removed ──►         [ -  │  20  │  30  ]
#
#  ── PEEK / FRONT (Inspect) ──
#
#    Step 1: Check for Queue Underflow (if isEmpty()).
#    Step 2: Return value at FRONT without modifying pointers or queue contents.
#
#  ── THE "FALSE OVERFLOW" PROBLEM & CIRCULAR QUEUE ──
#
#  In a simple fixed-size array, continuous enqueues and dequeues cause FRONT
#  and REAR to drift to the right. Even if slots are freed at the front,
#  REAR hits the array bound, creating a "False Overflow".
#
#  Solution -> CIRCULAR QUEUE:
#  Pointers wrap around using modulo arithmetic:
#      next_index = (current_index + 1) % capacity


# 5. TYPES OF QUEUES
#
#  1. SIMPLE / LINEAR QUEUE:
#     - Traditional FIFO queue.
#     - Insertion strictly at REAR, deletion strictly at FRONT.
#
#  2. CIRCULAR QUEUE:
#     - Last position connects back to the first position.
#     - Maximizes memory utilization in fixed-size arrays.
#
#  3. DOUBLE-ENDED QUEUE (DEQUE):
#     - Insertions and deletions supported at BOTH FRONT and REAR.
#     - Can function as both a Stack and a Queue.
#
#  4. PRIORITY QUEUE:
#     - Each element has an associated priority.
#     - Elements with highest priority are dequeued first, regardless of arrival.
#     - Typically implemented via a Binary Heap.


# 6. ADVANTAGES OF A QUEUE
#
#  ✔  Guaranteed Fairness: FIFO order prevents starvation (first come, first served).
#  ✔  Constant Time Operations: Enqueue, dequeue, and peek all operate in O(1).
#  ✔  Asynchronous Decoupling: Acts as a buffer between producers and consumers
#     operating at different speeds (e.g. rate-limiting, message queues).
#  ✔  Fundamental for Graph Algorithms: Enables Breadth-First Search (BFS),
#     shortest-path in unweighted graphs, and level-order tree traversals.
#  ✔  Order Preservation: Maintains original arrival sequence accurately.


# 7. DISADVANTAGES OF A QUEUE
#
#  ✘  No Random Access: Cannot access arbitrary elements by index (disallowed/O(n)).
#  ✘  Expensive Search: Finding a specific element requires O(n) traversal.
#  ✘  Memory Wastage in Simple Arrays: Linear array queues suffer from pointer
#     drifting ("false overflow") unless implemented as Circular Queues.
#  ✘  Fixed Capacity Limits: Array-based queues can overflow unless dynamically resized.
#  ✘  Pointer Overhead: Linked list implementations require extra memory for pointers.

