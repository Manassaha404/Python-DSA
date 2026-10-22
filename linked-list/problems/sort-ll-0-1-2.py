# Sort Linked List of 0s, 1s and 2s 
# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Time Complexity  : O(N) — single pass through the linked list of N nodes
# Space Complexity : O(N) — creates a new Node for each element (plus 3 dummy nodes); O(1) auxiliary space if nodes were relinked in-place
def segregate(head):
    if head is None:
        return head 
    zeroHead = Node(None)
    zeroTail = zeroHead 
    oneHead = Node(None)
    oneTail = oneHead 
    twoHead = Node(None)
    twoTail = twoHead
    curr = head 
    while curr is not None:
        new_node = Node(curr.data)
        if curr.data == 0:
            zeroTail.next = new_node 
            zeroTail = new_node 
        elif curr.data == 1:
            oneTail.next = new_node 
            oneTail = new_node
        else:
            twoTail.next = new_node 
            twoTail = new_node 
        curr = curr.next 
    zeroTail.next = oneHead.next if oneHead.next else twoHead.next
    oneTail.next = twoHead.next
    twoTail.next = None 
    return zeroHead.next