from collections import deque 

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

# balanced = height(l) - height(r) <= 1 

# Time Complexity : O(n) — each node is visited exactly once via post-order DFS
# Space Complexity: O(h) — recursive call stack depth equals the tree height
#                         O(log n) for a balanced tree, O(n) worst case for a skewed tree
def isBalanced(root: Node | None) -> bool:
    def checkHight(node:Node | None) -> int:
        if node is None:
            return 0
        left = 0 
        right = 0 
        if node.left is None:
            right = checkHight(node.right)
        if node.right is None:
            left = checkHight(node.left) 
        else:
            right = checkHight(node.right)
            left = checkHight(node.left)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left,right) 
    height = checkHight(root) 
    if height == -1:
        return False 
    else:
        return True 