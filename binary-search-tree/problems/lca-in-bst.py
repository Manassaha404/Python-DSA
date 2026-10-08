# Lowest Common Ancestor of a Binary Search Tree 
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/ 
#
# Time Complexity:  O(h) — at each node we move either left or right using BST
#                          property, traversing at most one root-to-leaf path;
#                          O(log n) balanced, O(n) skewed
# Space Complexity: O(h) — recursion call stack depth equals path length to LCA;
#                          O(log n) balanced, O(n) worst case (skewed tree)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root == p or root == q:
        return root 
    elif root.val < p.val and root.val > q.val:
        return root 
    elif root.val > p.val and root.val < q.val:
        return root 
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)