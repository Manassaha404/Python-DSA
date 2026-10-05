# Binary Tree Pruning 
# https://leetcode.com/problems/binary-tree-pruning/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pruneTree(root: TreeNode | None) -> TreeNode | None:
    # Time Complexity:  O(n) — every node is visited exactly once via post-order traversal
    # Space Complexity: O(h) — recursion stack depth equals tree height h
    #                   O(log n) for a balanced tree, O(n) worst case (skewed tree)
    def helper(node):
        if node is None:
            return False 
        lt = helper(node.left)
        rt = helper(node.right)
        if lt is False:
            node.left = None 
        if rt is False:
            node.right = None
        sf = True if node.val == 1 else False 
        return sf or lt or rt 
    r = helper(root)
    return root if r is True else None