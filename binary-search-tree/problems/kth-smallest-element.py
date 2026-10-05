# kth smallest element in BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Time Complexity:  O(h + k) — we traverse down to the leftmost node in O(h),
#                              then visit k nodes during the in-order traversal
#                              O(log n + k) for a balanced BST, O(n) worst case
# Space Complexity: O(h) — recursive call stack depth equals the tree height
#                          O(log n) balanced, O(n) worst case (skewed tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode | None, k: int) -> int:
    x = 1 
    ans = None 
    def helper(root):
        nonlocal x 
        nonlocal ans 
        if root.left:
            helper(root.left)
        if x == k:
            ans = root.val 
        x += 1 
        if root.right:
            helper(root.right)
    helper(root)
    return ans