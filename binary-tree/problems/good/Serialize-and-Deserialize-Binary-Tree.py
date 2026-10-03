# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/ 
class Node:
    def __init__(self, data):
        self.val = data
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



from collections import deque

# Overall complexities for both operations:
#   Time Complexity:  O(n) — every node is enqueued and processed exactly once.
#   Space Complexity: O(n) — the BFS queue holds at most O(n) nodes at a time (last
#                     level of a complete binary tree), and the serialized string /
#                     token list is proportional to the number of nodes.
class Codec:
    # Time Complexity:  O(n) — BFS visits each node exactly once.
    # Space Complexity: O(n) — queue stores at most O(n) nodes; output string grows to O(n).
    def serialize(self, root):
        output = ""
        if root is None:
            return output
        queue = deque([root])
        while queue:
            n = len(queue)            
            for i in range(n):
                node = queue.popleft()
                if node is None:
                    output += "#,"
                    continue
                output += str(node.val)
                output += ','
                queue.append(node.left)
                queue.append(node.right) 
        return output 
                
       
        

    # Time Complexity:  O(n) — BFS reconstructs each node exactly once.
    # Space Complexity: O(n) — queue stores at most O(n) nodes; token list is O(n).
    def deserialize(self, data):
        given = data.split(",")
        n = len(given)
        pointer = 0 
        if given[pointer] in ("#", ""):
            return 
        root = Node(int(given[pointer]))
        pointer += 1
        queue = deque([root])
        while queue and pointer <= n - 1:
            node = queue.popleft() 
            left = Node(int(given[pointer])) if given[pointer] != "#" else None
            pointer += 1 
            right = Node(int(given[pointer])) if given[pointer] != "#" or '' and pointer <= n - 1 else None
            pointer += 1
            node.left = left 
            node.right = right 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root 



