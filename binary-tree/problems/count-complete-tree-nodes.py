# Count Complete Tree Nodes 
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# Time Complexity : O(log²n)
#   - At each node, getLeftHeight and getRightHeight each traverse O(log n) levels.
#   - When left height == right height the subtree is a perfect binary tree and is
#     counted in O(1) without further recursion.
#   - In the worst case the recursion goes O(log n) levels deep, and at each level
#     we do O(log n) work → total O(log n × log n) = O(log²n).
#
# Space Complexity : O(log n)
#   - The recursion call stack is bounded by the height of the tree.
#   - For a complete binary tree height = O(log n) → O(log n) stack space.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def countNodes( root: TreeNode | None) -> int:
    def getLeftHight(node:TreeNode | None):
        count = 0
        while node:
            count += 1 
            node = node.left 
        return count 
    def getRightHight(node:TreeNode | None):
        count = 0
        while node:
            count += 1 
            node = node.right
        return count 
    def dfs(node: TreeNode) -> int:
        if node is None:
            return 0 
        lh = getLeftHight(node.left)
        rh = getRightHight(node.right) 
        if lh == rh:
            return (2**(lh + 1) - 1)
        else:
            return 1 + dfs(node.left) + dfs(node.right) 
    return dfs(root)


