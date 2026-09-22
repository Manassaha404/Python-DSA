# Boundary Traversal of Binary Tree

# Difficulty: Medium

# Problem Statement

# Given the root of a binary tree, return the values of the nodes
#  that lie on the boundary of the tree, in anti-clockwise order starting from the root.

# The boundary consists of (in order, without duplicating any node):

# The root node (unless the tree has only one node).
# The left boundary — the left-most nodes on each level, from top to bottom, excluding leaf nodes.
# The leaf nodes — from left to right.
# The right boundary — the right-most nodes on each level, from bottom to top, excluding leaf nodes.

# Definitions:

# The left boundary is defined as the path starting from the root's left subtree, always choosing the leftmost child if it exists, and if not, the right child. This excludes leaves.
# The right boundary is the mirror of that on the right subtree, then reversed.
# A node is a leaf if it has no left or right child.
# If the root itself is a leaf, it should only be output once (as the root), not duplicated as a leaf.

# Example 1
# Input: root = [1,null,2,3,4]

#         1
#          \
#           2
#          / \
#         3   4

# Output: [1,3,4,2]




class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


# Time Complexity: O(1) — just checks left/right child pointers.
# Space Complexity: O(1) — no extra space used.
def isLeaf(node:Node) -> bool:
    if node.left or node.right:
        return False 
    else:
        return True 

# Time Complexity: O(n) — left boundary traversal O(h), leaf collection O(n),
#                  right boundary traversal O(h); overall O(n) where n = total nodes.
# Space Complexity: O(n) — result list holds O(n) values; recursion stack for
#                  addLeafNodes is O(h) where h = height of the tree (O(log n)
#                  balanced, O(n) skewed).
def boundaryTraverse(root:Node | None) -> list[int]:
    if root is None:
        return [] 
    if isLeaf(root):
        return [root.val]
    result = [] 
    result.append(root.val)

    # left boundary 
    cur = root.left 
    while cur is not None:
        if isLeaf(cur) == False:
            result.append(cur.val)
        if cur.left:
            cur = cur.left 
        else:
            cur = cur.right 
    
    # leaf nodes
    # Time Complexity: O(n) — visits every node once to find leaves.
    # Space Complexity: O(h) — recursion stack depth equals tree height h.
    def addLeafNodes(node:Node | None):
        if node is None:
            return 
        nonlocal result
        if isLeaf(node):
            result.append(node.val)
        if node.left:
            addLeafNodes(node.left) 
        if node.right:
            addLeafNodes(node.right) 
    addLeafNodes(root) 

    # right boundary 
    temp = [] 
    cur = root.right 
    while cur is not None:
        if isLeaf(cur) == False:
            temp.append(cur.val)
        if cur.right:
            cur = cur.right 
        else:
            cur = cur.left
    temp.reverse() 
    result.extend(temp) 
    return result 
