# Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N) — single pass through the linked list of N nodes where each node is visited at most twice.
# Space Complexity : O(1) — in-place pointer manipulation using constant extra space.
def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    dummy = ListNode()
    temp = dummy
    curr = head
    while curr:
        val = curr.val
        if curr.next and curr.next.val == val:
            while curr.next and curr.next.val == val:
                curr = curr.next
        else:
            temp.next = curr
            temp = temp.next
        curr = curr.next
        temp.next = None
    return dummy.next