# Linked List Cycle II 
# https://leetcode.com/problems/linked-list-cycle-ii/description/ 

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None  
    slow = head 
    fast = head
    isCy = False 
    while fast.next and fast.next.next: 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            isCy = True
            break 
    if not isCy:
        return None 
    slow = head 
    while slow != fast:
        slow = slow.next 
        fast = fast.next 
    return slow