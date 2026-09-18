# Level-order traversal of a binary tree (BFS)
# Visits nodes level by level from left to right
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Time Complexity : O(n) — every node is enqueued and dequeued exactly once
# Space Complexity: O(w) — queue holds at most the widest level of the tree
#                         O(n/2) = O(n) worst case for a perfect binary tree
#                         O(1) best case for a skewed tree

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





from collections import deque 

def levelOrder(root: Node | None) -> list[list[int]]:
        output: list[list[int]] = []
        if root is None:
            return output
        queue = deque([root])          # initialise queue with root
        while queue:
            level: list[int] = []
            n = len(queue)             # number of nodes at current level
            for i in range(n):
                node = queue.popleft()     # O(1) dequeue
                level.append(node.val)
                if node.left:
                    queue.append(node.left)    # enqueue left child
                if node.right:
                    queue.append(node.right)   # enqueue right child
            output.append(level)
        return output



print(levelOrder(root))