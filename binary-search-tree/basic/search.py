# Search in a Binary Search Tree 
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# Time Complexity : O(H), where H is the height of the BST
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST
# Space Complexity: O(H) for the recursive call stack
#                  - O(log N) for a balanced BST
#                  - O(N) for a skewed (worst-case) BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None 
    if root.val == val:
        return root 
    elif root.right and val > root.val:
        return self.searchBST(root.right, val) 
    elif root.left:
        return self.searchBST(root.left, val) 
    else:
        return None