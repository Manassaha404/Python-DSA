# Minimum Depth of Binary Tree 
# https://leetcode.com/problems/minimum-depth-of-binary-tree/ 


from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque 
def minDepth(root: TreeNode | None) -> int:
    count = 0
    queue = deque() 
    if root:
        queue.append(root) 
        count += 1
    while queue:
        n = len(queue) 
        for i in range(n):
            node = queue.popleft() 
            if node.left == None and node.right == None:
                return count
            if node.left:
                queue.append(node.left)    
            if node.right:
                queue.append(node.right)
        count += 1 
    return count

# Time Complexity : O(n) — every node is enqueued and dequeued exactly once
# Space Complexity: O(w) — queue holds at most the widest level of the tree
#                         O(n/2) = O(n) worst case for a perfect binary tree
#                         O(1) best case for a skewed tree
