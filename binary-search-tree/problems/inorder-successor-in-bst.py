# Inorder Successor in BST 
# https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1 
#
# Time Complexity:  O(h) — only one root-to-leaf path is traversed at a time,
#                          exploiting BST property; O(log n) balanced, O(n) skewed
# Space Complexity: O(h) — recursion call stack depth proportional to tree height;
#                          O(log n) balanced, O(n) worst case (skewed tree)
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def inOrderSuccessor(root, k):
    successor = -1 
    def helper(node):
        if node is None:
            return 
        nonlocal k 
        nonlocal successor
        if node.data > k.data:
            successor = node.data 
            helper(node.left)
        elif node.data <= k.data:
            helper(node.right)
    helper(root)
    return successor

