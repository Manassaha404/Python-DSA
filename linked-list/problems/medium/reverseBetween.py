# Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N) — single pass to find the sublist boundaries up to right, followed by reversing at most N nodes
# Space Complexity : O(1) — in-place pointer manipulation using constant auxiliary space
def reverseBetween(head: ListNode | None, left: int, right: int) -> ListNode | None:
    leftNodeLeft = None
    leftNode = None
    rightNodeRight = None
    rightNode = None
    i = 1
    curr = head
    prev = None
    while curr:
        if i == left:
            leftNodeLeft = prev
            leftNode = curr
        if i == right:
            rightNode = curr
            rightNodeRight = curr.next
        i += 1
        prev = curr
        curr = curr.next
    if leftNodeLeft:
        leftNodeLeft.next = None
    rightNode.next = None

    def reverseList(head):
        if head is None:
            return None
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    reverseList(leftNode)
    if leftNodeLeft:
        leftNodeLeft.next = rightNode
    leftNode.next = rightNodeRight
    if leftNode == head:
        return rightNode
    return head