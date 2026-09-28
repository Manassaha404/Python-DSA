# Lowest Common Ancestor of a Binary Tree 
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/ 

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
def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
    # Time Complexity:  O(n) — in the worst case every node is visited once
    #                   (e.g. both p and q are in the leftmost subtree, forcing
    #                   a full traversal of the right subtree too).
    # Space Complexity: O(h) — the recursive call stack is at most h frames deep,
    #                   where h is the height of the tree.
    #                   Worst case (skewed tree): O(n). Balanced tree: O(log n).
    if root is None:
        return None  
    if root == p:
        return p
    if root == q:
        return q   
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right,p ,q) 
    if not left and not right:
        return None
    if left and right:
        return root
    else:
        return left if left else right