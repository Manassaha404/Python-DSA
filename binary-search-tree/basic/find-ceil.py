# Ceil in BST
# https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
#
# Time Complexity : O(H), where H is the height of the BST
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST
# Space Complexity: O(H) for the recursive call stack
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

def findCeil(root, x):
    ceil = -1 
    def helper(root):
        nonlocal ceil
        nonlocal x
        if root is None:
            return 
        if root.data >= x:
            ceil = root.data
            helper(root.left)
        elif root.right and x > root.data:
            helper(root.right) 
        elif root.left:
            helper(root.left) 
        else:
            return
    helper(root)
    return ceil