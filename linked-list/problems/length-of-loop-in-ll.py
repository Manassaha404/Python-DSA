# Cycle Length in Linked List 
# https://www.geeksforgeeks.org/problems/find-length-of-loop/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def lengthOfLoop(head):
    if head is None:
        return 0
    slow = head
    fast = head
    isCycle = False
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            isCycle = True
            break
    if isCycle is False:
        return 0
    curr = slow.next
    lenOfLoop = 1
    while curr != slow:
        curr = curr.next
        lenOfLoop += 1
    return lenOfLoop