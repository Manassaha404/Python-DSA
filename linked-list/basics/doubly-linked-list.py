# doubly linked list 





from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any = None,
                 next: Optional["Node"] = None,
                 prev: Optional["Node"] = None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = Node()  # dummy
        self.tail: Node = Node()  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size: int = 0

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self.size

    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        cur = self.head.next
        while cur is not self.tail:
            yield cur.value
            cur = cur.next

    # Time: O(1) | Space: O(1)  — O(1) because we maintain a tail pointer
    def append(self, value: Any):
        last = self.tail.prev
        new_node = Node(value, self.tail, last)
        last.next = new_node
        self.tail.prev = new_node
        self.size += 1

    # Time: O(1) | Space: O(1)
    def preAppend(self, value: Any):
        first = self.head.next
        new_node = Node(value, first, self.head)
        first.prev = new_node
        self.head.next = new_node
        self.size += 1

    # Time: O(1) | Space: O(1)
    def deleteFromHead(self):
        if self.size == 0:
            return
        curr = self.head.next
        self.head.next = curr.next
        curr.next.prev = self.head
        curr.next = None
        curr.prev = None
        self.size -= 1

    # Time: O(1) | Space: O(1)  — O(1) because tail.prev gives direct access
    def deleteFromBack(self):
        if self.size == 0:
            return
        curr = self.tail.prev
        self.tail.prev = curr.prev
        curr.prev.next = self.tail
        curr.next = None
        curr.prev = None
        self.size -= 1

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None
        self.size -= 1

    # Time: O(1) | Space: O(1)  — inserts just before the last real node
    def insertBeforeTail(self, value: Any):
        if self.size == 0:
            self.append(value)
            return
        last = self.tail.prev
        new_node = Node(value, last, last.prev)
        last.prev.next = new_node
        last.prev = new_node
        self.size += 1

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def insertAtIndex(self, value: Any, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        new_node = Node(value, curr, curr.prev)
        curr.prev.next = new_node
        curr.prev = new_node
        self.size += 1

    # https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
    # Time: O(n) | Space: O(1)  — swap next/prev on every node, dummies included
    def reverse(self):
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next, curr.prev = curr.prev, nxt
            curr = nxt
        self.head, self.tail = self.tail, self.head
                

    





    
    




dll = DoublyLinkedList()
dll.append(8)
dll.append(10)
dll.append(898)
dll.append(45) 
dll.preAppend(34)
print(len(dll))
dll.deleteFromHead() 
print(len(dll))
dll.deleteFromBack()
print(len(dll))
dll.deleteAtIndex(1)
dll.insertBeforeTail(67)
dll.insertAtIndex(7, 1)
dll.reverse() 
dll.append(100) 
for val in dll:
    print(val, end="->")
print("None") 

    

    

    