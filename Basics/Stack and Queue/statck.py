
# S T A C K

# CONCEPT:
#   A Stack is a linear data structure that follows the
#   LIFO principle — Last In, First Out.
#   Think of a stack of plates: you add/remove from the top.

# KEY PROPERTIES:
#   - Only the TOP element is accessible at any time.
#   - Two primary operations: push (add) & pop (remove).

# TIME COMPLEXITY:
#   - Push   : O(1)
#   - Pop    : O(1)
#   - Peek   : O(1)
#   - Search : O(n)
#
# SPACE COMPLEXITY: O(n)


stack = []  # Initialize an empty stack

# Push — add element to top
stack.append(10)  # stack: [10]
stack.append(20)  # stack: [10, 20]
stack.append(30)  # stack: [10, 20, 30]

# Pop — remove and return top element
top = stack.pop()       # removes 30 → top = 30

# Peek — view top element without removing
peek = stack[-1]        # 20 (does not remove)

# Check if stack is empty
is_empty = len(stack) == 0   # False

# Size — number of elements
size = len(stack)       # 2

# Clear — remove all elements
stack.clear()           # stack: []

# Check again after clear
is_empty = len(stack) == 0   # True

print("Top after pop :", top)       # 30
print("Peek          :", peek)      # 20
print("Size          :", size)      # 2
print("Is empty      :", is_empty)  # True
