# Delete the Middle Node of a Linked List 
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/ 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time Complexity  : O(N) — single pass where fast pointer reaches the end in N/2 iterations
# Space Complexity : O(1) — in-place pointer manipulation using a constant number of pointers
def deleteMiddle(head: ListNode | None) -> ListNode | None:
    prev = None 
    slow = head 
    fast = head 
    while fast and fast.next:
        fast = fast.next.next 
        prev = slow
        slow = slow.next 
    delNode = slow 
    if slow == head:
        head = slow.next 
    else:
        prev.next = slow.next 
    del delNode 
    return head