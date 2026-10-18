
# What is a Node in a Linked List?
# A Node is the fundamental building block of a Linked List.

# Each node contains two parts:
#
#   1. DATA -> The actual value/data stored in the node.
#   2. NEXT -> A reference (pointer) to the next node in the list.
#
# Visual Representation:
#   [ data | next ] --> [ data | next ] --> [ data | next ] --> None
#     Head                                    Tail (next = None)
#
# Key Points:
#   - The first node is called the HEAD of the linked list.
#   - The last node's `next` pointer is None (marks end of list).
#   - Unlike arrays, nodes are NOT stored in contiguous memory.
#   - Each node points to the next, forming a chain.


class Node:
    def __init__(self, data):
        self.data = data   # The value stored in this node
        self.next = None   # Pointer to the next node (initially None)

    def __repr__(self):
        return f"Node({self.data})"