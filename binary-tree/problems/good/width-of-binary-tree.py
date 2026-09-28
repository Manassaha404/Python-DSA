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
class nodeIndex:
    def __init__(self, node:Node,index:int):
        self.node = node 
        self.index =  index
def widthOfBinaryTree(root: Node | None) -> int:
    # Time Complexity:  O(n) — every node is visited exactly once via BFS.
    # Space Complexity: O(w) — the queue holds at most one full level of nodes,
    #                   where w is the maximum width of the tree.
    #                   Worst case (complete/perfect binary tree): O(n/2) = O(n).
    #                   Note: index values use relative offsets (el.index - minIndex)
    #                   to prevent integer overflow in wide trees.
    if root is None:
        return 0 
    queue = deque([nodeIndex(root, 0)])
    maxlength = 0
    while queue:
        size = len(queue)
        minIndex = queue[0].index 
        leftMostIndex = minIndex 
        rightMostIndex = queue[size - 1].index
        maxlength = max(maxlength, rightMostIndex-leftMostIndex+1)
        for i in range(size):
            el = queue.popleft()
            if el.node.left:
                queue.append(nodeIndex(el.node.left, 2*(el.index - minIndex) + 1))
            if el.node.right:
                queue.append(nodeIndex(el.node.right, 2*(el.index - minIndex) + 2)) 
        
    return maxlength

print(widthOfBinaryTree(root))
            

        

