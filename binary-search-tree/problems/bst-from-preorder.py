# Construct Binary Search Tree from Preorder Traversal 
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/ 
#
# Time Complexity:  O(n) — each element in preorder is processed exactly once
# Space Complexity: O(n) — recursion call stack depth is O(h), where h is the
#                          height of the BST; worst case O(n) for a skewed tree,
#                          O(log n) for a balanced BST. Output tree itself is O(n).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def bstFromPreorder(preorder: list[int]) -> TreeNode | None:
    def constructNode(val, up):
        if val < up:
            return TreeNode(val)
        else:
            return None 
    maxi = float("inf")
    pointer = 0 
    n = len(preorder) - 1 
    root = constructNode(preorder[pointer], maxi)
    pointer += 1 
    def helper(up, root):
        nonlocal pointer
        nonlocal n 
        if pointer > n:
            return 
        left = constructNode(preorder[pointer], root.val)
        if left:
            root.left = left 
            pointer += 1 
            helper(root.val, root.left)
        if pointer > n:
            return 
        right = constructNode(preorder[pointer], up)
        if right:
            root.right = right 
            pointer += 1 
            helper(up, root.right) 
    helper(maxi, root)
    return root