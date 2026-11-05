# Middle of the Linked List 
# https://leetcode.com/problems/middle-of-the-linked-list/description/ 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode | None) -> ListNode | None:
    # Slow & Fast Pointer Approach:
    # Time Complexity  : O(n) — fast pointer traverses the list once (n/2 steps)
    # Space Complexity : O(1) — only two pointers used, no extra data structures
    slow = head 
    fast = head 
    # for second middle for even number of nodes  
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    # for first middle for even number of nodes
    # while fast.next and fast.next.next:
    #     slow = slow.next 
    #     fast = fast.next.next 
    return slow