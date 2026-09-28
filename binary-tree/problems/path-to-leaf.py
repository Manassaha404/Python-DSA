# https://leetcode.com/problems/binary-tree-paths/ 
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




def binaryTreePaths(root: Node | None) -> list[str]:
    # Time Complexity:  O(n * h) — every node is visited once (O(n)), and at each
    #                   leaf we join the path list into a string in O(h) time.
    #                   Worst case (skewed): O(n²). Balanced: O(n log n).
    # Space Complexity: O(n * h) — the call stack depth is O(h), and `paths` stores
    #                   one list per root-to-leaf path, each of length O(h).
    #                   Worst case (skewed): O(n²). Balanced: O(n log n).
    if root is None:
        return [] 
    paths = [] 

    def helper(node:Node, path = []):
        nonlocal paths
        path.append(str(node.val)) 
        if node.left == None and node.right == None:
            paths.append(path) 
            return 
        elif node.left is not None and node.right is not None:
            helper(node.left, path.copy())
            helper(node.right, path.copy())
            return 
        elif node.left is not None:
            helper(node.left, path)
            return 
        else:
            helper(node.right, path) 
            return
    helper(root)
    result = [] 
    for path in paths:
        result.append("->".join(path))

    return result 



print(binaryTreePaths(root))