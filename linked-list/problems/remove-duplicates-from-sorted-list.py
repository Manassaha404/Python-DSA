# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N) — single pass traversing all N nodes of the sorted linked list.
# Space Complexity : O(1) — in-place pointer modification with constant auxiliary space.
def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    prev = head
    curr = head.next
    while curr:
        if prev.val == curr.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head