# same tree 
# https://leetcode.com/problems/same-tree/description/ 

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

# Time Complexity  : O(N) — visits every node in both trees exactly once (N = min nodes)
# Space Complexity : O(H) — recursive call stack depth equals tree height H
#                   O(log N) for a balanced tree, O(N) worst case (skewed tree)
def isSameTree(self, p: Node | None, q: Node | None) -> bool:
    if p == None or q == None:
        return (p == q)                                         # one or both subtrees exhausted
    return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 