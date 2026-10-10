# Largest BST Subtree
# https://www.geeksforgeeks.org/problems/largest-bst/1
#
# Overall Complexity:
#   Time : O(n) — every node is visited exactly once during the post-order traversal.
#   Space: O(h) — recursion stack depth equals the tree height h
#           (O(log n) balanced, O(n) worst-case skewed).

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Bst:
    def __init__(self, size, largest, smallest):
        self.size = size
        self.largest = largest
        self.smallest = smallest

def largestBst(root: 'Node') -> int:
    # Time : O(n) — single post-order traversal visits each node once.
    # Space: O(h) — implicit recursion stack; h is the height of the tree.
    maxSize = 0

    def postOrder(node):
        # Time : O(1) per call (excluding recursive subcalls)
        # Space: O(1) extra per call; total recursion depth is O(h)
        nonlocal maxSize
        if node is None:
            # Base case: empty subtree is a valid BST of size 0.
            # largest = -inf so any real node is larger → left BST check passes.
            # smallest = +inf so any real node is smaller → right BST check passes.
            return Bst(0, float("-inf"), float("inf"))
        left = postOrder(node.left)
        right = postOrder(node.right)
        if left.largest < node.data < right.smallest:
            size = left.size + right.size + 1
            maxSize = max(maxSize, size)
            largest = max(right.largest, node.data)
            smallest = min(left.smallest, node.data)
            return Bst(size, largest, smallest)
        else:
            # Subtree rooted at node is NOT a valid BST.
            # Return sentinel values that will cause parent's BST check to fail.
            return Bst(0, float("inf"), float("-inf"))

    postOrder(root)
    return maxSize
