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



# without recursion (BFS / Level-order)
# Time Complexity : O(n) — every node is enqueued and dequeued exactly once
# Space Complexity: O(w) — queue holds at most one full level of the tree
#                         O(n/2) = O(n) worst case for a perfect binary tree (widest level)
#                         O(1) best case for a completely skewed tree
def maxDepth(root: Node | None) -> int:
    if root is None:
        return 0 
    queue = deque([root])
    depth = 0
    while queue:
        n = len(queue) 
        for i in range(n):
            node = queue.popleft() 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
        depth += 1 
    return depth

# with recursion (DFS)
# recurrence relation -> 1 + max(l,r) 
# Time Complexity : O(n) — every node is visited exactly once
# Space Complexity: O(h) — recursive call stack depth equals the tree height
#                         O(log n) for a balanced tree, O(n) worst case for a skewed tree
def maxDepth(root: Node | None) -> int:
    if root is None:
        return 0 
    if root.left is None:
        return 1 + maxDepth(root.right) 
    elif root.right is None:
        return 1 + maxDepth(root.left) 
    else:
        return 1 + max(maxDepth(root.left),maxDepth(root.right))

