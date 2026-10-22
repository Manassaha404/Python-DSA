# Add Two Numbers 
# https://leetcode.com/problems/add-two-numbers/description/ 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time Complexity  : O(max(N, M)) — where N and M are the lengths of l1 and l2 (at most max(N, M) + 1 iterations)
# Space Complexity : O(max(N, M)) — to store the newly created result linked list (O(1) auxiliary space)
def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    ll1 = l1 
    ll2 = l2 
    sumListHead = None 
    sumListTail = None
    carry = 0 
    while ll1 or ll2 or carry:
        s = (ll1.val if ll1 else 0) + (ll2.val if ll2 else 0 ) + carry 
        carry = s // 10 
        new_node = ListNode(s % 10)
        if sumListHead:  
            sumListTail.next = new_node
            sumListTail = new_node 
        else:
            sumListHead = new_node 
            sumListTail = new_node 
        ll1 = ll1.next if ll1 else None  
        ll2 = ll2.next if ll2 else None
    return sumListHead