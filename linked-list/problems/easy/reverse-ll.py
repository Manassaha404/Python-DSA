# Reverse Linked List 
# https://leetcode.com/problems/reverse-linked-list/description/ 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: ListNode | None) -> ListNode | None:
    # Iterative Approach (commented out):
    # Time Complexity  : O(n) — single pass through all n nodes
    # Space Complexity : O(1) — only a constant number of pointers used
    # if head is None:
    #     return None 
    # prev = None 
    # curr = head 
    # while curr:
    #     temp = curr.next 
    #     curr.next = prev 
    #     prev = curr 
    #     curr = temp 
    # return prev

    # Recursive Approach (active):
    # Time Complexity  : O(n) — visits every node once via recursion
    # Space Complexity : O(n) — recursive call stack grows up to n frames
    def helper(node):
        if node is None or node.next is None:
            return node 
        newHead = helper(node.next)
        front = node.next 
        front.next = node
        node.next = None 
        return newHead 
    return helper(head)





