# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N + M) — where N and M are the lengths of list1 and list2; traverses both lists at most once
# Space Complexity : O(1) — merges the lists in-place using constant auxiliary space
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    temp1 = list1
    temp2 = list2
    dummy = ListNode()
    curr = dummy
    while temp1 and temp2:
        if temp1.val > temp2.val:
            curr.next = temp2
            temp2 = temp2.next
        else:
            curr.next = temp1
            temp1 = temp1.next
        curr = curr.next
    if temp1:
        curr.next = temp1
    if temp2:
        curr.next = temp2
    return dummy.next