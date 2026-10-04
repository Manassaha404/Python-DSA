# Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
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

def insertIntoBST(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return TreeNode(val) 
    def insert(node):
        nonlocal val
        if val > node.val:
            if node.right:
                insert(node.right)
            else:
                node.right = TreeNode(val) 
                return 
        else:
            if node.left:
                insert(node.left)
            else:
                node.left = TreeNode(val)
                return 
    insert(root)
    return root


