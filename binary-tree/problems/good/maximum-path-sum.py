# Binary Tree Maximum Path Sum 
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/ 


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


def maxPathSum(root: Node | None) -> int:
    maxi = root.val 
    def helper(node: Node | None):
        nonlocal maxi 
        if node == None:
            return 0 
        maxLeft = helper(node.left)   # max gain from left subtree
        maxRight = helper(node.right) # max gain from right subtree
        maxi = max(maxi, (node.val + maxLeft + maxRight))  # path through current node
        return max(node.val + max(maxLeft, maxRight, 0), 0)  # best single-branch gain to parent
    helper(root) 
    return maxi





