# Linked List Cycle II 
# https://leetcode.com/problems/linked-list-cycle-ii/description/ 

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time Complexity  : O(N) — where N is the number of nodes; Floyd's Cycle-Finding Algorithm takes linear time to detect loop and find the start node
# Space Complexity : O(1) — uses two pointers with constant auxiliary space
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