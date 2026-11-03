# Reorder List
# https://leetcode.com/problems/reorder-list/description/
# Time Complexity  : O(N) — where N is the number of nodes; one pass to push nodes onto the stack and at most N/2 iterations to relink nodes
# Space Complexity : O(N) — auxiliary stack stores all N nodes of the linked list
def reorderList(head: ListNode | None) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    curr = head
    stack = []
    while curr:
        stack.append(curr)
        curr = curr.next
    curr = head
    while curr:
        nextCurr = curr.next
        node = stack.pop()
        if node == curr or node == nextCurr:
            node.next = None
            return
        else:
            curr.next = node
            node.next = nextCurr
            curr = nextCurr
    return