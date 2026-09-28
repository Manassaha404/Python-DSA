# Binary Tree Right Side View 
# https://leetcode.com/problems/binary-tree-right-side-view/description/
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
from collections import deque 
class Coordinates:
    def __init__(self, node:TreeNode, vertical:int, horizontal:int):
        self.node = node 
        self.vertical = vertical
        self.horizontal = horizontal 

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # Time Complexity:  O(n log n) — O(n) to visit every node via BFS +
        #                   O(h log h) for sorted(elementMap.keys()) where h = tree height.
        #                   In the worst case (skewed tree) h = n, making it O(n log n).
        # Space Complexity: O(n) — the queue holds at most one full level of nodes (O(w),
        #                   where w is max width ≤ n/2), elementMap stores one entry per node,
        #                   and the result list stores one value per level (O(h)).
        #                   Overall dominated by O(n) for elementMap.
        if root is None:
            return []
        queue = deque([Coordinates(root, 0, 0)])
        result = []
        elementMap = {}
        while queue:
            n = len(queue)
            for i in range(n):
                element = queue.popleft()
                node = element.node
                vertical_level = element.vertical
                horizontal_level = element.horizontal
                if horizontal_level not in elementMap:
                    elementMap[horizontal_level] = {
                        vertical_level:node.val
                    }
                if node.right:
                    queue.append(Coordinates(node.right, vertical_level + 1, horizontal_level + 1))
                if node.left:
                    queue.append(Coordinates(node.left, vertical_level - 1, horizontal_level + 1))
        for horizontal_level in sorted(elementMap.keys()):
            elementHorizontalOrderMap = elementMap[horizontal_level]
            for vertical_level in elementHorizontalOrderMap:
                element = elementHorizontalOrderMap[vertical_level]
                result.append(element) 
        return result