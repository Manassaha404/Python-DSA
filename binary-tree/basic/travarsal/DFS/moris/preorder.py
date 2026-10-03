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


# Time Complexity:  O(n) — each node is visited at most twice (once when setting
#                   the thread, once when removing it), so total work is O(n).
# Space Complexity: O(1) — no recursion stack or auxiliary stack is used; the tree's
#                   right pointers are temporarily modified (threads) and then restored,
#                   using only a constant number of extra pointers at any time.
#                   (The output list itself is O(n), but that is not counted as auxiliary space.)
def morrisPreorderTraversal(root: Node | None) -> list[int]:
    result: list[int] = [] 
    current = root
    while current is not None:
        if current.left is None:
            result.append(current.data)
            current = current.right 
        else:
            prev = current.left 
            while prev.right is not None and prev.right is not current:
                prev = prev.right
            if prev.right is None:
                result.append(current.data)
                prev.right = current
                current = current.left
            else:
                prev.right = None
                current = current.right
    return result
