# Floor in BST 
# https://www.geeksforgeeks.org/problems/closest-neighbor-in-bst/1
#
# Time Complexity : O(H), where H is the height of the BST
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST
# Space Complexity: O(H) for the recursive call stack
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def findMaxFloor(root, k):
    floor = -1 
    def helper(root):
        nonlocal floor
        nonlocal k
        if root is None:
            return 
        if root.data <= k:
            floor = root.data
            helper(root.right)
        elif root.right and k > root.data:
            helper(root.right) 
        elif root.left:
            helper(root.left) 
        else:
            return
    helper(root)
    return floor

