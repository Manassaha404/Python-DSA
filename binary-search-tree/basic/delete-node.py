# delete node in a binary search tree
# https://leetcode.com/problems/delete-node-in-a-bst/description/

# Time Complexity:  O(h) — searching for the key and finding the rightmost node of the
#                          left subtree each take O(h), where h is the tree height.
#                          O(log n) for a balanced BST, O(n) in the worst case (skewed tree)
# Space Complexity: O(h) — recursive call stack for searchBST and findExtremeRight
#                          O(log n) balanced, O(n) worst case
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: TreeNode | None, key: int) -> TreeNode | None:
    if root is None:
        return None
    def findExtremeRight(node):
        if node.right is None:
            return node 
        return findExtremeRight(node.right) 
    def helper(node):
        if node.left is None:
            return node.right 
        elif node.right is None:
            return node.left 
        elif node.left is None and node.right is None:
            return None 
        else:
            rightChild = node.right 
            lastRight = findExtremeRight(node.left) 
            lastRight.right = rightChild
            return node.left
    if root.val == key:
        return helper(root)
    def searchBST(root: TreeNode, val: int):
        if root is None:
            return 
        if val > root.val:
            if root.right and root.right.val == val:
                root.right = helper(root.right)
                return 
            else:
                searchBST(root.right, val) 
        else:
            if root.left and root.left.val == val:
                root.left = helper(root.left)
                return  
            else:
                searchBST(root.left, val)
    searchBST(root, key)
    return root