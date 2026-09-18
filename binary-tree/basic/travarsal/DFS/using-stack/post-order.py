# Example: building a small tree manually
#         1
#        / \
#       2   3
#      / \
#     4   5

class Node:
    def __init__(self, data:int):
        self.data = data
        self.left = None
        self.right = None 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

# Time Complexity : O(n) — every node is visited exactly once
# Space Complexity: O(h) — stack holds at most h nodes at a time, where h is the tree height
#                         O(log n) for a balanced tree, O(n) worst case for a skewed tree
def postorder(root:Node):
    result = [] 
    el = root 
    stack = [] 
    while len(stack) != 0 or el is not None:
        if el is not None:
            stack.append(el)
            el = el.left
        else:
            top = stack[len(stack) - 1]
            temp = top.right
            if temp is not None:
                el = temp 
            else:
                temp = stack.pop() 
                result.append(temp.data) 
                while len(stack) != 0 and temp == stack[len(stack) - 1].right:
                    temp = stack.pop()
                    result.append(temp.data) 
    return result
 
print(postorder(root))


