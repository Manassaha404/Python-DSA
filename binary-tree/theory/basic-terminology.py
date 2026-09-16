# TREE DATA STRUCTURE 
# -------------------   




# Below is a sample tree diagram that will be referred to throughout
# these explanations:
#
#                         A     <- Root
#                       /   \
#                      B     C
#                    /   \     \
#                   D     E     F
#                 /   \
#                G     H
#
# (G, H, E, F are Leaf Nodes - they have no children)




# 1. WHAT IS A TREE? 
# A tree is a non-linear, hierarchical data structure made up of
# "nodes" connected by "edges". It starts from a single node called
# the root and branches out into child nodes, forming a structure
# that looks like an upside-down real-life tree. 

# Key properties of a tree: 
#   - It has exactly ONE root node.
#   - Every node (except the root) has exactly ONE parent.
#   - There are no cycles/loops (you can't go in a circle).
#   - It is a connected structure - every node is reachable from root.


# Example (general tree, a node can have any number of children):
#
#                         A
#                      /  |  \
#                     B   C   D
#                    / \       \
#                   E   F       G
#
# Here A is connected to B, C, D; B is connected to E, F; and so on. 



# 2. WHAT IS A NODE? 
# A node is a single element/unit in a tree. Each node typically
# stores:
#   - Some data/value
#   - A reference/pointer to its child node(s) 

# In the diagram below, A, B, C, D, E, F, G are ALL nodes.
#
#                         A   <- node
#                       /   \
#                      B     C   <- nodes
#                    /   \
#                   D     E      <- nodes



# 3. WHAT IS THE ROOT? 
# The root is the topmost node of the tree. It is the only node that
# has no parent. Every other node in the tree can be reached by
# starting from the root and moving downward. 
#
#                       [A]   <- ROOT (topmost node, no parent)
#                      /   \
#                     B     C
#                    / \
#                   D   E




# 4. WHAT ARE CHILDREN? 
# Children are the nodes directly connected below a given node, one
# level down. A node that has children is called that node's
# "parent".
#
#                         A
#                       /   \
#                      B     C     <- B and C are CHILDREN of A
#                    /   \
#                   D     E        <- D and E are CHILDREN of B
#
# So: A is the parent of B and C.
#     B is the parent of D and E. 




# 5. WHAT ARE ANCESTORS? 
# Ancestors of a node are all the nodes that lie on the path from
# that node UP to the root (its parent, grandparent, and so on,
# all the way to the root). 
#
#                         A
#                       /   \
#                      B     C
#                    /   \
#                   D     E
#
# Ancestors of E: B, A   (go up from E -> B -> A)
# Ancestors of D: B, A   (go up from D -> B -> A)
# Ancestors of B: A      (go up from B -> A)
# Ancestors of A: (none, A is the root) 




# 6. WHAT IS A SUBTREE? 
# A subtree is any node in the tree along with all of its
# descendants (children, grandchildren, etc.). Essentially, if you
# pick any node and look at everything hanging below it, that
# smaller tree-shaped piece is a subtree.
#
#                         A
#                       /   \
#                      B     C
#                    /   \
#                   D     E
#
# The subtree rooted at B looks like this (taken out separately):
#
#                      B
#                    /   \
#                   D     E
#
# So {B, D, E} together form the "subtree rooted at B".
# Similarly {C} alone is the subtree rooted at C (since C has no
# children here), and the WHOLE tree {A, B, C, D, E} is the subtree
# rooted at A.



# 7. WHAT ARE LEAF NODES? 
# A leaf node (or just "leaf") is a node that has NO children. It is
# an "end point" of the tree - nothing branches out further from it.
#
#                         A
#                       /   \
#                      B     C
#                    /   \     \
#                   D     E     F   <- D, E, F have no children
#
# Here D, E, and F are LEAF NODES because none of them have any
# children below them. A, B, C are NOT leaves because they each have
# at least one child. 


# 8. WHAT IS A BINARY TREE?
# A binary tree is a special type of tree where EVERY node has AT
# MOST TWO children. These two children are usually called the
# "left child" and the "right child". 


#                         A
#                       /   \
#                  (left)  (right)
#                      B       C
#                    /   \       \
#                   D     E       F

# Rules of a binary tree:
#   - Each node has 0, 1, or 2 children only (never more than 2).
#   - Children are distinguished as "left child" and "right child". 

# Example showing a node with only a left child (no right child):
#
#                         A
#                        /
#                       B         <- B is the LEFT child of A,
#                                    A has no right child

# Binary trees are the foundation for many other structures like
# Binary Search Trees (BST), Heaps, AVL Trees, etc. 

# QUICK SUMMARY (all terms, using the same diagram) 
#
#                         A                <- Root (no parent)
#                       /   \
#                      B     C             <- Children of A
#                    /   \     \
#                   D     E     F          <- D,E children of B;
#                                              F child of C
#
#   Nodes            : A, B, C, D, E, F  (every element in the tree)
#   Root             : A
#   Children of A    : B, C
#   Ancestors of E    : B, A
#   Subtree at B      : { B, D, E }
#   Leaf nodes        : D, E, F  (no children of their own)
#   Binary Tree       : true here, since no node has more than
#                        2 children



