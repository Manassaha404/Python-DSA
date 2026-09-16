# Pre-order traversal of a binary tree
# (Root, Left, Right)
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# Time Complexity : O(n) — every node is visited exactly once
# Space Complexity: O(h) — recursion call stack depth equals tree height h
#                         O(log n) for a balanced tree, O(n) worst case (skewed tree)
def preorder(node):
    if node is None:       # base case
        return
    print(node.data, end=" ")  # visit root
    preorder(node.left)    # recurse left subtree
    preorder(node.right)   # recurse right subtree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example: building a small tree manually
#         1
#        / \
#       2   3
#      / \
#     4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 

preorder(root) 