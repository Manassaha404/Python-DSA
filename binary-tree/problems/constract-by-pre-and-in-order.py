# Construct Binary Tree from Preorder and Inorder Traversal 
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ 
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


def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    inOrderHash = {}
    preOrderLength = len(preorder) 
    inOrderLength = len(inorder) 
    for i in range(inOrderLength):
        inOrderHash[inorder[i]] = i 
    def buildTree(preStart, preEnd, inStart, inEnd):
        nonlocal preorder
        nonlocal inorder
        nonlocal inOrderHash
        if (inStart > inEnd or preStart > preEnd):
            return None
        elVal = preorder[preStart]
        inOrderIndex = inOrderHash[elVal]
        leftSize = inOrderIndex - inStart
        # left sub tree
        leftInStart = inStart
        leftInEnd = inOrderIndex - 1 
        leftPreStart = preStart + 1 
        leftPreEnd = preStart + leftSize
        leftTree = buildTree(leftPreStart, leftPreEnd, leftInStart, leftInEnd)

        # right sub tree 
        rightInStart = inOrderIndex + 1
        rightInEnd = inEnd
        rightPreStart = leftPreEnd + 1
        rightPreEnd = preEnd
        rightTree = buildTree(rightPreStart, rightPreEnd, rightInStart, rightInEnd)
        root = TreeNode(preorder[preStart], leftTree, rightTree)
        return root 
    root = buildTree(0, preOrderLength - 1, 0, inOrderLength - 1)
    return root