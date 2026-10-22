# Odd Even Linked List 
# https://leetcode.com/problems/odd-even-linked-list/description/ 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity  : O(N) — single pass through the linked list of N nodes
# Space Complexity : O(1) — in-place pointer manipulation, no extra nodes or memory allocated
def oddEvenList(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head 
    oddCurr = head 
    evenCurr = oddCurr.next 
    evenCurrHead = evenCurr 
    while oddCurr.next and evenCurr.next:
        oddCurr.next = evenCurr.next 
        oddCurr = evenCurr.next  
        evenCurr.next = oddCurr.next 
        evenCurr = oddCurr.next
    oddCurr.next = evenCurrHead 
    return head