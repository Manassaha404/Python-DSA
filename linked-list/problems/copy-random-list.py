# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



from typing import Optional
# Time Complexity  : O(N) — two linear passes over the linked list of N nodes (one to copy nodes and map them, another to link random pointers)
# Space Complexity : O(N) — hash map stores mappings for all N nodes
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    dummy = Node(0)
    temp = dummy
    nodeHashMap = {}
    curr = head
    while curr:
        new_node = Node(curr.val)
        nodeHashMap[curr] = new_node
        temp.next = new_node
        temp = temp.next
        curr = curr.next
    curr = head
    temp = dummy.next
    while curr:
        randomNode = curr.random
        if randomNode is not None:
            newCopyNode = nodeHashMap[randomNode]
            temp.random = newCopyNode
        curr = curr.next
        temp = temp.next
    return dummy.next