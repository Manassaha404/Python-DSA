# check bst or not 
# https://leetcode.com/problems/validate-binary-search-tree/description/ 

# Time Complexity:  O(n) — every node is visited exactly once
# Space Complexity: O(h) — recursive call stack depth equals the height of the tree
#                          O(log n) for a balanced BST, O(n) in the worst case (skewed tree)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode | None) -> bool:
    maxi = float("inf")
    mini = float("-inf")
    def helper(node, maxi, mini):
        if node.val >= maxi or node.val <= mini:
            return False 
        lt = True 
        rt = True 
        if node.left:
            lt = helper(node.left, node.val, mini)
        if node.right:
            rt = helper(node.right, maxi, node.val)
        if lt and rt:
            return True 
        else:
            return False 
    return helper(root, maxi,mini)

