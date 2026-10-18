
# =============================================================================
#                        LINKED LIST — THEORY & CONCEPTS
# =============================================================================


# -----------------------------------------------------------------------------
# 1. WHAT IS A LINKED LIST?
# -----------------------------------------------------------------------------
#
# A Linked List is a linear data structure where elements (called NODES) are
# stored in memory NON-CONTIGUOUSLY and connected via POINTERS.
#
# Unlike arrays, a linked list does NOT use index-based access.
# Instead, you traverse from one node to the next using the `next` pointer.
#
# Visual Representation (Singly Linked List):
#
#   HEAD
#    |
#    v
#   [ 10 | * ] --> [ 20 | * ] --> [ 30 | * ] --> None
#                                   ^
#                                  TAIL
#
# Each box represents a NODE:  [ data | next_pointer ]


# -----------------------------------------------------------------------------
# 2. TYPES OF LINKED LISTS
# -----------------------------------------------------------------------------
#
#  a) SINGLY LINKED LIST
#     - Each node has one pointer: `next` (points to the next node).
#     - Traversal is ONE direction only (head → tail).
#
#     [ A | * ] --> [ B | * ] --> [ C | None ]
#
#  b) DOUBLY LINKED LIST
#     - Each node has TWO pointers: `prev` and `next`.
#     - Traversal is possible in BOTH directions.
#
#     None <-- [ A | * ] <--> [ B | * ] <--> [ C | None ]
#
#  c) CIRCULAR LINKED LIST
#     - The TAIL node's `next` points back to the HEAD (no None at end).
#     - Can be singly or doubly circular.
#
#     [ A | * ] --> [ B | * ] --> [ C | * ]
#          ^________________________________|
#
#  d) CIRCULAR DOUBLY LINKED LIST
#     - Combination of doubly + circular.
#     - Tail.next = Head  AND  Head.prev = Tail.


# -----------------------------------------------------------------------------
# 3. KEY TERMINOLOGY
# -----------------------------------------------------------------------------
#
#   HEAD  → The first node in the list. Entry point for traversal.
#   TAIL  → The last node in the list. Its `next` is None (or Head if circular).
#   NODE  → Individual element containing data + pointer(s).
#   NULL  → Marks the end of the list (None in Python).
#   SIZE  → Total count of nodes in the list.


# -----------------------------------------------------------------------------
# 4. MEMORY LAYOUT — Arrays vs Linked Lists
# -----------------------------------------------------------------------------
#
#  ARRAY  (contiguous memory):
#  ┌───┬───┬───┬───┬───┐
#  │ 1 │ 2 │ 3 │ 4 │ 5 │   ← stored side-by-side in RAM
#  └───┴───┴───┴───┴───┘
#    0   1   2   3   4     ← index-based O(1) random access
#
#  LINKED LIST (scattered memory):
#  [ 1 | 0x200 ]   [ 2 | 0x450 ]   [ 3 | None ]
#    addr:0x100       addr:0x200      addr:0x450
#
#  Nodes live at random addresses; each knows only its own data + next address.


# -----------------------------------------------------------------------------
# 5. CORE OPERATIONS & TIME COMPLEXITIES
# -----------------------------------------------------------------------------
#
#  Operation               Singly LL       Doubly LL       Array
#  ─────────────────────────────────────────────────────────────
#  Access by index         O(n)            O(n)            O(1)
#  Search                  O(n)            O(n)            O(n)
#  Insert at HEAD          O(1)            O(1)            O(n)
#  Insert at TAIL          O(1)*           O(1)            O(1) amortized
#  Insert at middle        O(n)            O(n)            O(n)
#  Delete at HEAD          O(1)            O(1)            O(n)
#  Delete at TAIL          O(n)            O(1)            O(1) amortized
#  Delete at middle        O(n)            O(n)            O(n)
#  Space                   O(n)            O(n)            O(n)
#
#  * O(1) tail insert requires maintaining a `tail` pointer.


# -----------------------------------------------------------------------------
# 6. OPERATIONS — HOW THEY WORK (STEP BY STEP)
# -----------------------------------------------------------------------------
#
#  ── PREPEND (Insert at HEAD) ──
#
#  Before:  HEAD → [20] → [30] → None
#  Insert:  10
#
#  Step 1: Create new node: [10 | None]
#  Step 2: new_node.next = current HEAD  →  [10 | *] → [20] → [30] → None
#  Step 3: HEAD = new_node
#
#  After:   HEAD → [10] → [20] → [30] → None
#
#  ── APPEND (Insert at TAIL) ──
#
#  Before:  HEAD → [10] → [20] → None   (TAIL = [20])
#  Insert:  30
#
#  Step 1: Create new node: [30 | None]
#  Step 2: current TAIL.next = new_node
#  Step 3: TAIL = new_node
#
#  After:   HEAD → [10] → [20] → [30] → None   (TAIL = [30])
#
#  ── DELETE at HEAD ──
#
#  Before:  HEAD → [10] → [20] → [30] → None
#
#  Step 1: HEAD = HEAD.next   →   HEAD now points to [20]
#  Step 2: old head is garbage collected (Python handles this)
#
#  After:   HEAD → [20] → [30] → None
#
#  ── DELETE at TAIL (Singly LL) ──
#
#  Before:  HEAD → [10] → [20] → [30] → None
#
#  Step 1: Traverse to the node BEFORE tail (second-to-last): [20]
#  Step 2: second_last.next = None
#  Step 3: TAIL = second_last
#
#  After:   HEAD → [10] → [20] → None   (requires O(n) traversal)
#
#  ── SEARCH ──
#
#  Traverse from HEAD, compare each node's value to target.
#  Stop when found or when None is reached.   →   O(n)


# -----------------------------------------------------------------------------
# 7. ADVANTAGES OF LINKED LISTS
# -----------------------------------------------------------------------------
#
#  ✔  Dynamic size — grows/shrinks at runtime without reallocation.
#  ✔  Efficient insertions/deletions at the HEAD: O(1).
#  ✔  No memory waste from pre-allocation (unlike arrays with fixed capacity).
#  ✔  Basis for other data structures: Stacks, Queues, Graphs, Hash tables.


# -----------------------------------------------------------------------------
# 8. DISADVANTAGES OF LINKED LISTS
# -----------------------------------------------------------------------------
#
#  ✘  No random access — must traverse from HEAD: O(n) to reach index i.
#  ✘  Extra memory per node for the pointer(s).
#  ✘  Poor cache locality — nodes scattered in memory (arrays are cache-friendly).
#  ✘  Reverse traversal is expensive in singly linked lists.


# -----------------------------------------------------------------------------
# 9. WHEN TO USE A LINKED LIST?
# -----------------------------------------------------------------------------
#
#  USE Linked List when:
#   - Frequent insertions/deletions at the front or middle.
#   - Size of data is unknown / highly dynamic.
#   - Implementing Stacks, Queues, or LRU Cache.
#   - No need for random index-based access.
#
#  PREFER Array/List when:
#   - You need O(1) random access by index.
#   - Data size is fixed or mostly static.
#   - Cache performance matters (e.g., math-heavy computations).


# -----------------------------------------------------------------------------
# 10. COMMON LINKED LIST PROBLEMS (DSA Patterns)
# -----------------------------------------------------------------------------
#
#  Pattern                         Example Problems
#  ──────────────────────────────────────────────────────────────────
#  Two Pointers (slow & fast)    → Detect cycle, Find middle, Nth from end
#  Reversal                      → Reverse list, Reverse in k-groups
#  Merge / Sort                  → Merge two sorted lists, Sort list
#  Dummy Node Trick              → Remove nth node, Merge sorted lists
#  Recursive Thinking            → Reverse recursively, Deep copy with random ptr
#  Runner Technique              → Palindrome check, Reorder list
#
#  Cycle Detection (Floyd's Algorithm):
#
#   slow = head          # moves 1 step at a time
#   fast = head          # moves 2 steps at a time
#
#   If fast and slow ever MEET → cycle exists.
#   If fast reaches None       → no cycle.
#
#  Finding the MIDDLE NODE:
#
#   slow = head
#   fast = head
#   while fast and fast.next:
#       slow = slow.next
#       fast = fast.next.next
#   # slow is now at the middle


# -----------------------------------------------------------------------------
# 11. LINKED LIST vs OTHER DATA STRUCTURES
# -----------------------------------------------------------------------------
#
#  Data Structure   Insert   Delete   Access   Search   Notes
#  ──────────────────────────────────────────────────────────────────────
#  Array            O(n)     O(n)     O(1)     O(n)     Cache friendly
#  Linked List      O(1)*    O(1)*    O(n)     O(n)     * at known node
#  Stack (LL)       O(1)     O(1)     O(n)     O(n)     LIFO
#  Queue (LL)       O(1)     O(1)     O(n)     O(n)     FIFO
#  Hash Table       O(1) avg O(1) avg O(1) avg O(1) avg Uses LL for chaining


# -----------------------------------------------------------------------------
# 12. PYTHON-SPECIFIC NOTES
# -----------------------------------------------------------------------------
#
#  - Python's built-in `list` is a DYNAMIC ARRAY, NOT a linked list.
#  - `collections.deque` is implemented as a DOUBLY LINKED LIST internally.
#      → Use deque for O(1) appendleft() and popleft() instead of list.
#
#  - In Python, there are no explicit pointers; object references act as pointers.
#  - Memory management (garbage collection) is automatic.
#
#  Example using collections.deque (built-in doubly linked list):
#
#   from collections import deque
#   dq = deque([1, 2, 3])
#   dq.appendleft(0)   # O(1) — insert at front
#   dq.popleft()       # O(1) — remove from front
#   dq.append(4)       # O(1) — insert at back
#   dq.pop()           # O(1) — remove from back


# -----------------------------------------------------------------------------
# 13. QUICK REFERENCE CHEAT SHEET
# -----------------------------------------------------------------------------
#
#  Linked List Cheat Sheet
#  ────────────────────────────────────────────────────
#  Type          Nodes         Direction      Circular?
#  ────────────────────────────────────────────────────
#  Singly        data + next   Forward only   No
#  Doubly        data+prev+next Both ways     No
#  Circular      data + next   Forward only   Yes
#  Circ. Doubly  data+prev+next Both ways     Yes
#  ────────────────────────────────────────────────────
#
#  Complexities (Singly LL with head & tail pointers):
#  ───────────────────────────────────────────────────
#  prepend()   →  O(1)
#  append()    →  O(1)
#  delete_head →  O(1)
#  delete_tail →  O(n)   ← need to find second-to-last
#  search()    →  O(n)
#  access(i)   →  O(n)
#  ───────────────────────────────────────────────────

