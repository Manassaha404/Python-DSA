# Remove Linked List Elements 
# https://leetcode.com/problems/remove-linked-list-elements/ 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time Complexity  : O(N) — single pass traversing all N nodes of the linked list
# Space Complexity : O(1) — in-place removal using a dummy node and constant auxiliary pointers
def removeElements( head: ListNode | None, val: int) -> ListNode | None:
    dummy = ListNode(-1, head)
    temp = dummy.next 
    prev = dummy
    while temp:
        if temp.val == val:
            prev.next = temp.next
        else:
            prev = temp 
        temp = temp.next 
    return dummy.next