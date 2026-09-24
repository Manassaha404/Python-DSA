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
        

# Time Complexity : O(n log n) — BFS visits each of the n nodes once O(n),
#                   but sorting the vertical columns at the end costs O(n log n)
#                   in the worst case (all nodes in distinct columns).
# Space Complexity: O(n) — the BFS queue holds at most O(n) nodes at once,
#                   and elementMap stores all n node values across all columns.
def verticalTraversal(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    # Each entry in the queue carries the node plus its (vertical, horizontal) coordinates.
    # vertical  : column index (left child → col-1, right child → col+1)
    # horizontal: depth/row index (both children → row+1)
    queue = deque([Coordinates(root, 0, 0)])
    result = []
    # elementMap: { vertical_col → { horizontal_row → [node values] } }
    elementMap = {}

    while queue:
        element = queue.popleft()
        node = element.node
        vertical_level = element.vertical
        horizontal_level = element.horizontal

        # Group node value by its (vertical, horizontal) coordinate
        if vertical_level in elementMap:
            elementVerticalOrderMap = elementMap[vertical_level]
            if horizontal_level in elementVerticalOrderMap:
                elementCounter = elementVerticalOrderMap[horizontal_level]
                elementCounter.append(node.val)
            else:
                elementVerticalOrderMap[horizontal_level] = [node.val]
        else:
            elementMap[vertical_level] = {
                horizontal_level: [node.val]
            }

        # Enqueue children with updated coordinates
        if node.left:
            queue.append(Coordinates(node.left, vertical_level - 1, horizontal_level + 1))
        if node.right:
            queue.append(Coordinates(node.right, vertical_level + 1, horizontal_level + 1))

    # Flatten each vertical column (row order is preserved by BFS)
    for vertical_level in sorted(elementMap.keys()):
        level = [] 
        elementVerticalOrderMap = elementMap[vertical_level]
        for horizontal_level in sorted(elementVerticalOrderMap):
            elementCounter = elementVerticalOrderMap[horizontal_level]
            for x in sorted(elementCounter):
                level.append(x) 
        result.append(level) 
    return result 




        





