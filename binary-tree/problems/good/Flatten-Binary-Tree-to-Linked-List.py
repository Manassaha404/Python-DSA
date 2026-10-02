# Flatten Binary Tree to Linked List 
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/ 
#
# Time Complexity : O(n)
#   - The helper function performs a reverse post-order traversal (right → left → root),
#     visiting each node exactly once → O(n).
#
# Space Complexity : O(h)  (implicit call stack only; no extra data structures)
#   - The recursion depth equals the height h of the tree.
#     • Best/Average (balanced tree): O(log n)
#     • Worst (skewed tree / already flattened): O(n)
#   - No additional data structures are used; modification is done in-place.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: TreeNode | None) -> None:
    prev = None 
    def helper(node:TreeNode | None) -> None:
        nonlocal prev
        if node is None:
            return 
        helper(node.right) 
        helper(node.left) 
        node.right = prev
        node.left = None 
        prev = node 
    helper(root)