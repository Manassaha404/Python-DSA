class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque 
class Coordinates:
    def __init__(self, node:TreeNode, vertical:int, horizontal:int):
        self.node = node 
        self.vertical = vertical
        self.horizontal = horizontal 

class Solution:
    # Time Complexity : O(n log n) — BFS visits every node once O(n);
    #                   sorted() on the column keys costs O(w log w) where w
    #                   is the width of the tree (w ≤ n), so overall O(n log n).
    # Space Complexity: O(n) — BFS queue holds O(n) nodes in the worst case,
    #                   and elementMap stores one entry per unique column (≤ n columns).
    def topView(self, root):
        if root is None:
            return []

        # Each queue entry carries (node, vertical_col, horizontal_row).
        # vertical  : column index — left child → col-1, right child → col+1
        # horizontal: depth/row   — both children → row+1
        queue = deque([Coordinates(root, 0, 0)])
        result = []
        # elementMap: { vertical_col → { horizontal_row → node.val } }
        # Only the FIRST node seen per column is stored (BFS guarantees top-most node comes first).
        elementMap = {}

        while queue:
            element = queue.popleft()
            node = element.node
            vertical_level = element.vertical
            horizontal_level = element.horizontal

            # Top-view rule: record only the first (topmost) node for each column
            if vertical_level not in elementMap:
                elementMap[vertical_level] = {
                    horizontal_level: node.val
                }

            # Enqueue children with updated coordinates
            if node.left:
                queue.append(Coordinates(node.left, vertical_level - 1, horizontal_level + 1))
            if node.right:
                queue.append(Coordinates(node.right, vertical_level + 1, horizontal_level + 1))

        # Collect results left-to-right by sorting column keys
        for vertical_level in sorted(elementMap.keys()):
            elementVerticalOrderMap = elementMap[vertical_level]
            for horizontal_level in elementVerticalOrderMap:
                element = elementVerticalOrderMap[horizontal_level]
                result.append(element)
        return result