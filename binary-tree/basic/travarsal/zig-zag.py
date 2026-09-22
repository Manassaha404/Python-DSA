# Binary Tree Zigzag Level Order Traversal 
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/ 


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

from collections import deque

# Time Complexity: O(n) — every node is enqueued and dequeued exactly once,
#                  and each level list may be reversed in O(k) where k = nodes
#                  at that level; total reversals still sum to O(n).
# Space Complexity: O(n) — the queue holds at most O(w) nodes at a time (w =
#                  max width of the tree); the result list stores all n values.
#                  In the worst case (complete binary tree) w = n/2, so O(n).
def zigzagLevelOrder(root: Node | None) -> list[list[int]]:
        result:list[list[int]] = [] 
        if root is None:
            return result
        queue = deque([root])
        flag = 0 # 0 -> go right, 1 -> go left 
        while queue:
            n = len(queue) 
            level = [] 
            for i in range(n):
                node = queue.popleft() 
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right) 
                level.append(node.val) 
            if flag == 0:
                result.append(level)
                flag = 1
            else:
                level.reverse()
                result.append(level)
                flag = 0
        return result



