# All Nodes Distance K in Binary Tree 
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/ 
#
# Time Complexity : O(n)
#   - Phase 1 (BFS to build parent map): visits every node once → O(n).
#   - Phase 2 (BFS from target): in the worst case visits every node once → O(n).
#   - Note: the `not in visitedNodes` checks use a list, making each check O(n),
#     so the overall complexity could degrade to O(n²) in the worst case.
#     Using a set for visitedNodes would keep it at O(n).
#
# Space Complexity : O(n)
#   - O(n) for the parentNodeHash dictionary.
#   - O(n) for the visitedNodes list and the BFS queue.
#   - Overall: O(n).

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque 


def distanceK( root: TreeNode, target: TreeNode, k: int) -> list[int]:
    parentNodeHash = {
        root: None 
    } 
    queue = deque([root])
    while queue:
        n = len(queue) 
        for i in range(n):
            node = queue.popleft() 
            if node.left:
                parentNodeHash[node.left] = node 
                queue.append(node.left) 
            if node.right:
                parentNodeHash[node.right] = node
                queue.append(node.right)   
    distance = 0 
    queue = deque([target])
    visitedNodes = [] 
    result = [] 
    while queue:
        n = len(queue) 
        if distance == k:
            for i in range(n):
                node = queue.popleft() 
                result.append(node.val) 
            break
        for i in range(n):
            node = queue.popleft()
            visitedNodes.append(node) 
            parrentNode = parentNodeHash.get(node) 
            if parrentNode is not None and parrentNode not in visitedNodes:
                queue.append(parrentNode) 
            if node.left and node.left not in visitedNodes:
                queue.append(node.left) 
            if node.right and node.right not in visitedNodes:
                queue.append(node.right) 
        distance += 1 
    return result