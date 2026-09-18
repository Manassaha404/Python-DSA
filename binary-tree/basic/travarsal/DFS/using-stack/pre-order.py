class Node:
    def __init__(self, data:int):
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

# Time Complexity : O(n) — every node is visited exactly once
# Space Complexity: O(h) — stack holds at most h nodes at a time, where h is the tree height
#                         O(log n) for a balanced tree, O(n) worst case for a skewed tree
def preOrder(root:Node) -> list[int]: 
    stack = [root]  
    result = [] 
    while len(stack) != 0:
        node = stack.pop() 
        result.append(node.data) 
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left) 
    return result 

print(preOrder(root))  

