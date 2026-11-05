# Add 1 to a Linked List Number 
# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1 



class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Time Complexity  : O(N) — where N is the number of nodes; three passes (reverse, add carry, reverse back)
# Space Complexity : O(1) — in-place modification using constant pointers, at most one node allocated for carry overflow
def addOne(head):
    carry = 1 
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
    head = reverseList(head)
    curr = head 
    while curr:
        if carry == 1 and curr.data == 9:
            curr.data = 0 
            carry = 1 
            curr = curr.next
        elif carry == 1 and curr.data != 9:
            curr.data = curr.data + carry 
            carry = 0
            break
    head = reverseList(head)
    if carry == 1:
        new_node = Node(1) 
        new_node.next = head 
        head = new_node
    return head