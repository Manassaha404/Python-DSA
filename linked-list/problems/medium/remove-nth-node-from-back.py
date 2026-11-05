# Remove Nth Node From End of List 
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    # Two-Pointer (fast & slow) Approach:
    # Time Complexity  : O(n) — two passes at most: one to advance fast by n,
    #                    one more to reach the end; overall linear in list length
    # Space Complexity : O(1) — only a constant number of pointers used
    count = 1
    fast = head 
    while count <= n:
        fast = fast.next 
        count += 1 
    slow = head 
    if fast is None:
        return slow.next
    while fast and fast.next:
        fast = fast.next 
        slow = slow.next 
    slow.next = slow.next.next if slow.next else None 
    return head