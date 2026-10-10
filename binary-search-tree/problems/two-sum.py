# Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# Overall Complexity:
#   Time : O(n) — findTarget uses the two-pointer technique; each pointer advances at
#          most n times and each advance costs O(h) amortized → O(n) total.
#   Space: O(h) — both stacks (nextStack & beforeStack) each hold at most h nodes,
#          where h is the tree height (O(log n) balanced, O(n) worst-case skewed).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def putInNextStack(self, node):
        # Time : O(h) — pushes the node and all left descendants (in-order forward pointer)
        # Space: O(h) — recursion depth equals the height of the subtree
        if node is None:
            return
        self.nextStack.append(node)
        self.putInNextStack(node.left)

    def putInBeforeStack(self, node):
        # Time : O(h) — pushes the node and all right descendants (in-order reverse pointer)
        # Space: O(h) — recursion depth equals the height of the subtree
        if node is None:
            return
        self.beforeStack.append(node)
        self.putInBeforeStack(node.right)

    def __init__(self, root: TreeNode | None):
        # Time : O(h) — initialises both stacks by traversing the leftmost and rightmost paths
        # Space: O(h) — each stack stores at most h nodes
        self.nextStack = []
        self.beforeStack = []
        self.putInNextStack(root)
        self.putInBeforeStack(root)

    def next(self) -> int:
        # Time : O(h) amortized — pop O(1) + putInNextStack on right child O(h);
        #        amortized O(1) over all n calls.
        # Space: O(h) — no extra allocation beyond the existing stack
        node = self.nextStack.pop()
        if node.right:
            self.putInNextStack(node.right)

    def before(self) -> int:
        # Time : O(h) amortized — pop O(1) + putInBeforeStack on left child O(h);
        #        amortized O(1) over all n calls.
        # Space: O(h) — no extra allocation beyond the existing stack
        node = self.beforeStack.pop()
        if node.left:
            self.putInBeforeStack(node.left)

    def hasNext(self) -> bool:
        # Time : O(1)  |  Space: O(1)
        return True if len(self.nextStack) != 0 else False

    def hasBefore(self) -> bool:
        # Time : O(1)  |  Space: O(1)
        return True if len(self.beforeStack) != 0 else False

    def getNext(self) -> int:
        # Time : O(1) — peek at the top of nextStack (smallest unvisited node)
        # Space: O(1)
        return self.nextStack[-1].val

    def getBefore(self) -> int:
        # Time : O(1) — peek at the top of beforeStack (largest unvisited node)
        # Space: O(1)
        return self.beforeStack[-1].val


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        # Time : O(n) — two-pointer approach; each of the n nodes is pushed/popped at most once.
        # Space: O(h) — the two iterator stacks each occupy O(h) space.
        obj = BSTIterator(root)
        while obj.hasNext() and obj.hasBefore():
            low = obj.getNext()
            high = obj.getBefore()
            if low == high:
                break
            s = low + high
            if s > k:
                obj.before()
            elif s < k:
                obj.next()
            else:
                return True
        return False