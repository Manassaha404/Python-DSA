# Rotate List
# https://leetcode.com/problems/rotate-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time Complexity  : O(N) — where N is the number of nodes in the linked list; one pass to find length and tail, and another pass to find the new split point
# Space Complexity : O(1) — modifies pointers in-place with constant auxiliary space
def rotateRight(head: ListNode | None, k: int) -> ListNode | None:
    if head is None:
        return head

    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    new_tail_position = length - (k % length)
    if new_tail_position != 0:
        tail.next = head

        position = 1
        new_tail = head
        while position != new_tail_position:
            new_tail = new_tail.next
            position += 1

        head = new_tail.next
        new_tail.next = None

    return head