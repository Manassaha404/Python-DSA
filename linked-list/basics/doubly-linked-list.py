# doubly linked list 

from typing import Any, Optional, Iterator


class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.prev = prev



class DoublyLinkedList:
    def __init__(self):
        self.head:Optional[Node] = None 
        self.tail:Optional[Node] = None 
        self.size:int = 0 

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self.size 

    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    # Time: O(1) | Space: O(1)  — O(1) because we maintain a tail pointer
    def append(self, value:Any):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node 
            self.tail = new_node 
        self.size += 1 

    # Time: O(1) | Space: O(1)
    def preAppend(self, value:Any):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node 
            self.tail = new_node
        else:
            new_node = Node(value, self.head, None)
            self.head.prev = new_node 
            self.head = new_node 
        self.size += 1 

    # Time: O(1) | Space: O(1)
    def deleteFromHead(self):
        if self.head is None:
            return 
        elif self.size == 1:
            self.head = None 
            self.tail = None 
        else:
            self.head.next.prev = None 
            curr = self.head 
            self.head = self.head.next 
            curr.next = None 
            del curr 
        self.size -= 1 

    # Time: O(1) | Space: O(1)  — O(1) because tail.prev gives direct access to the previous node
    def deleteFromBack(self):
        if self.tail is None:
            return 
        elif self.size == 1:
            self.head = None 
            self.tail = None
        else:
            self.tail.prev.next = None 
            curr = self.tail 
            self.tail = self.tail.prev 
            curr.prev = None 
            del curr 
        self.size -= 1 

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def deleteAtIndex(self, index:int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.deleteFromHead()
        elif index == self.size - 1:
            self.deleteFromBack()
        else:
            curr = self.head 
            count = 0 
            while count < index:
                curr = curr.next 
                count += 1 
            curr.prev.next = curr.next 
            curr.next.prev = curr.prev 
            curr.prev = None 
            curr.next = None 
            del curr 
            self.size -= 1

    # Time: O(1) | Space: O(1)  — O(1) because tail.prev gives direct access
    def insertBeforeTail(self, value:Any):
        if self.tail is None:
            new_node = Node(value)
            self.head = new_node 
            self.tail = new_node
            self.size += 1 
        elif self.tail == self.head:
            self.preAppend(value)
            return 
        else:
            new_node = Node(value, self.tail, self.tail.prev) 
            self.tail.prev.next = new_node
            self.tail.prev = new_node 
            self.size += 1 

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def insertAtIndex(self, value:Any, index:int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.preAppend(value) 
            return 
        elif index == self.size - 1:
            self.insertBeforeTail(value)
        else:
            curr = self.head 
            count = 0 
            while count < index:
                curr = curr.next 
                count += 1 
            new_node = Node(value, curr, curr.prev)
            curr.prev.next = new_node 
            curr.prev = new_node 
            self.size += 1 

    # https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1 
    # Time: O(n) | Space: O(1)  — O(n) to traverse and swap next/prev pointers for all nodes
    def reverse(self):
        if self.head is None:
            return 
        else:
            curr = self.head 
            self.tail = self.head
            while curr is not None:
                next = curr.next 
                curr.next = curr.prev 
                curr.prev = next 
                self.head = curr 
                curr = curr.prev 
                

    





    
    




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

    

    

    