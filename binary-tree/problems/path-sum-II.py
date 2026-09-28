# Path Sum II 
# https://leetcode.com/problems/path-sum-ii/
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


def pathSum(root: Node | None, targetSum: int) -> list[list[int]]:
    # Time Complexity:  O(n * h) — we visit every node once (O(n)) and at each leaf
    #                   we copy the current path which can be up to O(h) long.
    #                   In the worst case (skewed tree) h = n → O(n²).
    #                   For a balanced tree h = log n → O(n log n).
    # Space Complexity: O(n * h) — the recursive call stack is O(h) deep, and we
    #                   store up to O(n) paths each of length O(h) in `paths`.
    #                   Worst case (skewed): O(n²). Balanced: O(n log n).
    if root is None:
        return [] 
    paths = [] 
    def helper(node:Node,targetSum=targetSum, path = []):
        nonlocal paths
        if node == None:
            return 
        path.append(node.val) 
        targetSum -= node.val
        if node.left == None and node.right == None and targetSum == 0:
            paths.append(path) 
            return 
        elif node.left is not None and node.right is not None:
            helper(node.left,targetSum, path.copy())
            helper(node.right,targetSum, path.copy())
            return 
        helper(node.left,targetSum, path)
        helper(node.right,targetSum, path) 
    helper(root)
    return paths

print(pathSum(root, 8))