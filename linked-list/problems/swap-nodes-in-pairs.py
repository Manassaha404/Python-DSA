# Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N) — single pass traversing all N nodes in pairs (N/2 iterations)
# Space Complexity : O(1) — in-place pointer manipulation using constant auxiliary space
def swapPairs(self, head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    curr = head
    dummy = ListNode()
    temp = dummy
    while curr and curr.next:
        first = curr
        second = curr.next
        third = second.next
        second.next = first
        first.next = third
        temp.next = second
        temp = first
        curr = third
    return dummy.next