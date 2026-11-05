# Partition List
# https://leetcode.com/problems/partition-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity  : O(N) — single pass through the linked list of N nodes
# Space Complexity : O(1) — in-place pointer manipulation using two dummy nodes and constant auxiliary space
def partition( head: ListNode | None, x: int) -> ListNode | None:
    dummyLess = ListNode()
    dummyEqualAndGreater = ListNode()
    temp1 = dummyLess
    temp2 = dummyEqualAndGreater
    curr = head
    while curr:
        nextCurr = curr.next
        if curr.val < x:
            temp1.next = curr
            temp1 = temp1.next
            temp1.next = None
        else:
            temp2.next = curr
            temp2 = temp2.next
            temp2.next = None
        curr = nextCurr
    temp1.next = dummyEqualAndGreater.next
    return dummyLess.next