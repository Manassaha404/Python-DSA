# Maximum Binary Tree 
# https://leetcode.com/problems/maximum-binary-tree/description/ 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity:  O(n²) — at each recursive call we do a linear scan over the
#                   current sub-array to find the maximum (O(n) per level). In the
#                   worst case (already sorted input), the tree is a skewed chain and
#                   all n levels are visited, giving O(1 + 2 + ... + n) = O(n²).
#                   Average case on random input is O(n log n).
# Space Complexity: O(n) — the recursion stack depth equals the height of the
#                   constructed tree (O(log n) average, O(n) worst case for a skewed
#                   tree), plus O(n) for the n TreeNode objects created.
def constructMaximumBinaryTree( nums: list[int]) -> TreeNode | None:
    start = 0
    end = len(nums) - 1 
    def helper(start, end):
        nonlocal nums
        if end < start:
            return None
        rootVal = nums[start] 
        rootIndex = start 
        for i in range(start, end + 1):
            if nums[i] > rootVal:
                rootVal = nums[i]
                rootIndex = i 
        leftTree = helper(start, rootIndex - 1)
        rightTree = helper(rootIndex + 1, end) 
        root = TreeNode(rootVal, leftTree, rightTree)
        return root 
    return helper(start, end) 