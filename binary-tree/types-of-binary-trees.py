# 1. WHAT IS A BINARY TREE? 

# A binary tree is a special type of tree where EVERY node has AT
# MOST TWO children. These two children are usually called the
# "left child" and the "right child".
#
#                         A
#                       /   \
#                  (left)  (right)
#                      B       C
#                    /   \       \
#                   D     E       F
#
# Rules of a binary tree:
#   - Each node has 0, 1, or 2 children only (never more than 2).
#   - Children are distinguished as "left child" and "right child".
#
# Example showing a node with only a left child (no right child):
#
#                         A
#                        /
#                       B         <- B is the LEFT child of A,
#                                    A has no right child
#
# Binary trees are the foundation for many other structures like
# Binary Search Trees (BST), Heaps, AVL Trees, etc.

# 2. WHAT IS A FULL BINARY TREE? 

# A full binary tree (also called a "proper" or "strict" binary tree)
# is a binary tree in which EVERY node has EITHER 0 children OR
# EXACTLY 2 children. No node is allowed to have just 1 child.
#
#                         A
#                       /   \
#                      B     C
#                    /   \
#                   D     E
#
# Here: A has 2 children, B has 2 children, C has 0 children,
#       D has 0 children, E has 0 children.
# Every node has either 0 or 2 children -> this IS a full binary tree.
#
# Counter-example (NOT full, because B has only 1 child):
#
#                         A
#                       /   \
#                      B     C
#                     /
#                    D            <- B has only ONE child (D)
#                                    so this is NOT a full binary tree





# 3. WHAT IS A COMPLETE BINARY TREE? 

#
#                         A                <- level 0 (full)
#                       /   \
#                      B     C             <- level 1 (full)
#                    /   \   /
#                   D     E F              <- level 2 (filled left
#                                              to right, gap only
#                                              allowed at the end)
#
# Here the last level has D, E, F filled from left to right with no
# gaps before F -> this IS a complete binary tree.
#
# Counter-example (NOT complete, there's a gap on the left):
#
#                         A
#                       /   \
#                      B     C
#                       \
#                        E                 <- left child missing,
#                                              but right child (E)
#                                              present = gap on left
#                                              side -> NOT complete

# 11. WHAT IS A PERFECT BINARY TREE?

# A perfect binary tree is a binary tree where:
#   - ALL internal nodes have exactly 2 children, AND
#   - ALL leaf nodes are at the SAME level (same depth).
#   - Basically every level is completely and fully filled.
#
#                         A                <- level 0
#                       /   \
#                      B     C             <- level 1
#                    /   \   /   \
#                   D     E F     G        <- level 2 (all leaves,
#                                              all at same depth)
#
# Every level is fully filled and all leaves (D, E, F, G) are at the
# exact same depth -> this IS a perfect binary tree.
#
# Note: Every perfect binary tree is also a full binary tree AND a
# complete binary tree, but not the other way around.






# 12. WHAT IS A BALANCED BINARY TREE? (basic idea, not deep detail)

# A balanced binary tree is a binary tree where, for EVERY node, the
# height (depth) of its left subtree and right subtree differ by at
# most 1. In simple words: the tree doesn't lean heavily to one side,
# it stays roughly "even" in height on both sides.
#
# Example (balanced - heights of left/right subtrees are close):
#
#                         A
#                       /   \
#                      B     C
#                    /   \
#                   D     E
#
# Left subtree of A (B,D,E) has height 2, right subtree of A (C) has
# height 1. Difference is just 1 -> considered balanced.
#
# Counter-example (NOT balanced - very lopsided):
#
#                   A
#                  /
#                 B
#                /
#               C
#              /
#             D                    <- all nodes only on the left,
#                                      right side is empty at every
#                                      level -> heavily unbalanced



# 13. WHAT IS A DEGENERATE (OR PATHOLOGICAL) TREE?



# A degenerate tree is a tree where each parent node has ONLY ONE
# child (never two). This makes the tree behave essentially like a
# linked list - just a single long chain of nodes, with no real
# branching at all.
#
# Example (degenerate tree - all nodes chained to the right):
#
#                 A
#                  \
#                   B
#                    \
#                     C
#                      \
#                       D
#
# Example (degenerate tree - all nodes chained to the left):
#
#                       A
#                      /
#                     B
#                    /
#                   C
#                  /
#                 D
#
# Since there is no branching, a degenerate tree loses the main
# advantage of trees (fast searching) and behaves just like a
# linked list, making operations slower (O(n) instead of O(log n)).
