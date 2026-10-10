# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
#
# Overall Complexity:
#   Time  : O(n) amortized — each node is pushed and popped exactly once across
#           all next() calls, so n calls to next() cost O(n) total → O(1) amortized per call.
#   Space : O(h) — the stack holds at most h nodes at any time, where h is the
#           height of the tree (O(log n) for balanced, O(n) worst-case skewed).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def putInStack(self, node):
        # Time : O(h) — pushes the node and all its left descendants onto the stack
        # Space: O(h) — recursive call stack depth equals the height of the subtree
        if node is None:
            return
        self.stack.append(node)
        self.putInStack(node.left)

    def __init__(self, root: TreeNode | None):
        # Time : O(h) — calls putInStack which traverses the leftmost path
        # Space: O(h) — stack stores at most h nodes (leftmost path from root)
        self.stack = []
        self.putInStack(root)

    def next(self) -> int:
        # Time : O(h) amortized — pop is O(1); putInStack on right child is O(h).
        #        Amortized over all calls it is O(1) per call.
        # Space: O(h) — no extra space beyond the existing stack
        node = self.stack.pop()
        if node.right:
            self.putInStack(node.right)
        return node.val

    def hasNext(self) -> bool:
        # Time : O(1)
        # Space: O(1)
        return True if len(self.stack) != 0 else False


a = [8, 9]
print(a[-1])