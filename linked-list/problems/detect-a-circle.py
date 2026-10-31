# Linked List Cycle 
# 
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False 
    fast = head 
    slow = head 
    while fast.next and fast.next.next: 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False