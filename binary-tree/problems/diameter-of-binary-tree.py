class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example: building a small tree manually
#         1
#        / \
#       2   3
#      / \
#     4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# https://leetcode.com/problems/diameter-of-binary-tree/description/ 
# find the diameter of binary tree 
# for a node, diameter = left height + right height 
def diameterOfBinaryTree(root: Node | None) -> int:
    ans = 0
    def helper(node:Node | None):
        if node is None:
            return 0
        nonlocal ans 
        lh = helper(node.left) 
        rh = helper(node.right)
        ans =  max(ans, lh + rh)  
        return 1 + max(lh, rh) 
    helper(root) 
    return ans

