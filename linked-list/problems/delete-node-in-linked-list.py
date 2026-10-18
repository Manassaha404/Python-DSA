class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/ 
class Solution:
    # Approach: Copy-forward trick
    #   We are NOT given access to the head, so we can't traverse from the start.
    #   Instead, copy the NEXT node's value into the current node,
    #   then skip (unlink) the next node — effectively "deleting" current.
    #
    #   Before:  ... -> [node: 5] -> [next: 9] -> [9.next] -> ...
    #   Step 1 (copy):  [node: 9] -> [next: 9] -> [9.next] -> ...
    #   Step 2 (skip):  [node: 9] -> [9.next] -> ...
    #
    # Time  : O(1)  — no traversal, constant pointer operations
    # Space : O(1)  — no extra data structures used
    def deleteNode(self, node):
        # curr = node 
        # prev = None 
        # while curr != None:
        #     if curr.next is not None:
        #         prev = curr
        #         curr.val = curr.next.val 
        #     else:
        #         prev.next = None 
        #     curr = curr.next 
        if node is None or node.next is None:
            return        
        node.val = node.next.val 
        node.next = node.next.next 