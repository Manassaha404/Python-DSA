# Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# Overall Complexity:
#   Time : O(n) — a single in-order traversal visits every node exactly once.
#   Space: O(h) — recursion stack depth equals the tree height h
#           (O(log n) balanced, O(n) worst-case skewed).
#           Only O(1) extra variables are used (firstViolation, secondViolation, prev).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: TreeNode | None) -> None:
    # Time : O(n) — traverses all n nodes exactly once.
    # Space: O(h) — call stack depth; O(1) additional pointer variables.
    firstViolation = None
    firstViolationWith = None
    secondViolation = None
    prev = None

    def inorder(node):
        # Time : O(1) per call (excluding recursive subcalls)
        # Space: O(1) extra per call; total recursion depth is O(h)
        nonlocal firstViolation
        nonlocal firstViolationWith
        nonlocal secondViolation
        nonlocal prev
        if node is None:
            return
        inorder(node.left)
        if prev is not None:
            if prev.val > node.val:
                if firstViolation is None:
                    # First out-of-order pair found: record both nodes.
                    firstViolation = prev
                    firstViolationWith = node
                else:
                    # Second violation found: only the later node needs to be updated.
                    secondViolation = node
        prev = node
        inorder(node.right)

    inorder(root)

    # Swap the two misplaced nodes to restore BST property.
    # Case 1: two violations → nodes are far apart; swap firstViolation & secondViolation.
    # Case 2: one violation  → nodes are adjacent; swap firstViolation & firstViolationWith.
    if firstViolation and secondViolation:
        temp = firstViolation.val
        firstViolation.val = secondViolation.val
        secondViolation.val = temp
    else:
        temp = firstViolation.val
        firstViolation.val = firstViolationWith.val
        firstViolationWith.val = temp