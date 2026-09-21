# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).
# https://leetcode.com/problems/symmetric-tree/description/ 



from collections import deque 

class Node:
    def __init__(self, data):
        self.val = data
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

# Time Complexity  : O(N) — each node is visited exactly once via DFS
# Space Complexity : O(H) — recursive call stack depth equals tree height H
#                   O(log N) for a balanced tree, O(N) worst case (skewed tree)
def isSymmetric(root: Node | None) -> bool:
    if root.left == None and root.right == None:
        return True                                                          # single-node tree is symmetric
    def helper(left: Node | None, right: Node | None) -> bool:
        if left == None or right == None:
            return (left == right)                                           # both must be None to match
        return (left.val == right.val) and helper(left.left, right.right) and helper(left.right, right.left)
    return helper(root.left, root.right)

