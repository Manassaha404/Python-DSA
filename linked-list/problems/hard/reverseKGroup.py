# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time Complexity  : O(N) — where N is the number of nodes in the linked list; each node is processed a constant number of times (checked and reversed)
# Space Complexity : O(1) — reverses nodes in-place using pointers with constant auxiliary space
def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
    def reverseList(head: ListNode | None) -> ListNode | None:
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

    curr = head
    temp = curr
    val = 1
    prevTemp = None
    while curr:
        if val == k:
            nextNode = curr.next
            curr.next = None
            newHead = reverseList(temp)
            if prevTemp:
                prevTemp.next = newHead
            temp.next = nextNode
            if temp == head:
                head = newHead
            prevTemp = temp
            temp = nextNode
            curr = nextNode
            val = 0
        else:
            curr = curr.next
        val += 1
    return head