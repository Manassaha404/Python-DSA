#                           STACK — THEORY & CONCEPTS

# 1. WHAT IS A STACK?
#
# A Stack is a linear data structure that follows the LIFO principle:
#                "LAST IN, FIRST OUT" (or FILO: First In, Last Out)
#
# The element that is inserted LAST is the FIRST one to be removed.
# All insertions and deletions take place at ONE END only, called the TOP.
#
# Real-World Analogies:
#   - A stack of plates: You put a new plate on TOP and pick from the TOP.
#   - A stack of books on a desk.
#   - Undo / Redo feature in text editors (Ctrl + Z).
#   - Browser Back button history.
#   - Function call stack in program execution (recursion).
#
# Visual Representation:
#
#        PUSH (Insert)               POP (Remove)
#             │                           ▲
#             ▼                           │
#          ┌─────────────────────────────────┐
#          │              TOP                │ <── All actions happen here
#          ├─────────────────────────────────┤
#          │             Element 3           │
#          ├─────────────────────────────────┤
#          │             Element 2           │
#          ├─────────────────────────────────┤
#          │             Element 1           │
#          └─────────────────────────────────┘
#                         BOTTOM
#


# 2. KEY TERMINOLOGY
#
#
#   TOP         → Pointer or index referencing the most recently added element.
#   BOTTOM      → The base of the stack; the oldest inserted element.
#   PUSH        → Adding an element to the top of the stack.
#   POP         → Removing and returning the topmost element from the stack.
#   PEEK / TOP  → Viewing the topmost element WITHOUT removing it.
#   ISEMPTY     → Checking whether the stack has zero elements.
#   ISFULL      → Checking whether a fixed-size stack has reached capacity.
#   SIZE        → Total number of elements currently stored.
#   OVERFLOW    → Error state: attempting to PUSH into an already FULL stack.
#   UNDERFLOW   → Error state: attempting to POP or PEEK an EMPTY stack.


# 3. CORE OPERATIONS & TIME COMPLEXITIES
#
#  Operation       Time Complexity     Space Complexity    Description
#  ────────────────────────────────────────────────────────────────────────────
#  Push            O(1)                O(1)                Insert item onto TOP
#  Pop             O(1)                O(1)                Remove & return TOP
#  Peek / Top      O(1)                O(1)                Inspect TOP element
#  isEmpty         O(1)                O(1)                Check if size == 0
#  Size            O(1)                O(1)                Get count of items
#  Search          O(n)                O(1)                Search for an item
#  Access (by idx) O(n)*               O(1)                *Stack restricts access
#  ────────────────────────────────────────────────────────────────────────────
#  Overall Space:  O(n) to store n elements.
#
#  Note: In a pure abstract stack, random access by index is disallowed.
#        To reach the i-th element, you must pop elements above it.


# 4. OPERATIONS — HOW THEY WORK (STEP BY STEP)
#
#  ── PUSH (Insert) ──
#  Stack capacity: 4 (initially holding [10, 20])
#
#    Step 1: Check for Stack Overflow (if size == capacity).
#    Step 2: Place new item on top.
#    Step 3: Update TOP pointer.
#
#    Before:            Push(30):               After:
#     |      |          |  30  |  <-- new       |      |
#     |  20  | <--TOP   |  20  |                |  30  | <--TOP
#     |  10  |          |  10  |                |  20  |
#     +------+          +------+                |  10  |
#                                               +------+
#
#  ── POP (Remove) ──
#
#    Step 1: Check for Stack Underflow (if isEmpty()).
#    Step 2: Read value at TOP.
#    Step 3: Remove top element & decrement TOP pointer.
#    Step 4: Return value.
#
#    Before:            Pop() returns 30:       After:
#     |  30  | <--TOP   |  30  |  --> popped    |      |
#     |  20  |          |  20  |                |  20  | <--TOP
#     |  10  |          |  10  |                |  10  |
#     +------+          +------+                +------+
#
#  ── PEEK / TOP (Inspect) ──
#
#    Step 1: Check for Stack Underflow (if isEmpty()).
#    Step 2: Return value at TOP WITHOUT modifying the stack.



# 5. ADVANTAGES OF A STACK
#
#  ✔  Constant Time Operations: Push, Pop, and Peek execute in O(1) time.
#  ✔  Simple & Focused Interface: Restricts arbitrary access, preventing bugs.
#  ✔  Efficient Memory Management: Memory is allocated/freed as needed.
#  ✔  Natural Reversal: Processing items via stack naturally reverses order.
#  ✔  Hardware & Language Native: Underpins computer architecture (call stack).


# 6. DISADVANTAGES OF A STACK
#
#  ✘  No Random Access: Cannot directly read element at index `i` (O(n) work).
#  ✘  Risk of Overflow: Fixed-size stacks can exhaust allocated capacity.
#  ✘  Risk of Underflow: Popping an empty stack raises exceptions.
#  ✘  Limited Search Capability: Must empty elements to search within the stack.