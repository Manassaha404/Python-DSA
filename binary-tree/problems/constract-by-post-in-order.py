# Construct Binary Tree from Inorder and Postorder Traversal 
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# Time Complexity : O(n)
#   - Building the inorder hash map takes O(n).
#   - The recursive buildTree visits each node exactly once → O(n) total calls.
#   - Each call does O(1) work thanks to the hash map lookup (no slicing).
#
# Space Complexity : O(n)
#   - O(n) for the inorder hash map.
#   - O(h) for the recursion call stack, where h is the tree height.
#     • Best/Average (balanced tree): O(log n)
#     • Worst (skewed tree): O(n)
#   - Overall dominated by the hash map → O(n).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    inOrderHash = {}
    postOrderLength = len(postorder) 
    inOrderLength = len(inorder) 
    for i in range(inOrderLength):
        inOrderHash[inorder[i]] = i
    def buildTree(postStart, postEnd, inStart, inEnd):
        nonlocal postorder
        nonlocal inorder
        nonlocal inOrderHash
        if inStart == inEnd and postStart == postEnd:
            return TreeNode(postorder[postEnd], None, None)
        if (inStart > inEnd or postStart > postEnd):
            return None
        rootVal = postorder[postEnd]
            
        rootIndex = inOrderHash[rootVal]
        leftSize = rootIndex - inStart

        #left subtree 
        leftInStart = inStart 
        leftInEnd = rootIndex - 1
        leftPostStart = postStart 
        leftPostEnd = postStart + leftSize - 1
        leftTree = buildTree(leftPostStart, leftPostEnd, leftInStart, leftInEnd)

        #right subtree 
        rightInStart = rootIndex + 1
        rightInEnd = inEnd
        rightPostStart = leftPostEnd + 1 
        rightPostEnd = postEnd - 1 
        rightTree = buildTree(rightPostStart, rightPostEnd, rightInStart, rightInEnd)
        root = TreeNode(rootVal, leftTree, rightTree)
        return root 
    root = buildTree(0, postOrderLength - 1, 0, inOrderLength - 1)
    return root 

        