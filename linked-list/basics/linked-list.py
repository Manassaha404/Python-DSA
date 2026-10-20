from typing import Any, Iterator, Optional
class Node:
    def __init__(self, value: Any, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0
    
    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self._size
    
    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    # Time: O(1) | Space: O(1)
    def prepend(self, value: Any) -> None:
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self._size += 1 

    # Time: O(1) | Space: O(1)  — O(1) because we maintain a tail pointer
    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node 
        self._size += 1

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def insert(self, value: Any, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
        elif index == self._size - 1:
            self.append(value)
        else:    
            curr = self.head
            count = 0
            while count < index - 1:
                curr = curr.next 
                count += 1 
            node = Node(value, curr.next)
            curr.next = node 
            self._size += 1 
    # Time: O(1) | Space: O(1)
    def deleteAtFirst(self) -> None:
        if self.tail == self.head:
            self.tail = None
        self.head = self.head.next
        self._size -= 1 
    # Time: O(n) | Space: O(1)  — O(n) to reach the second-to-last node
    def deleteAtEnd(self) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None 
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next 
            curr.next = None 
            self.tail = curr
        self._size -= 1
    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.deleteAtFirst()
        elif index == self._size - 1:
            self.deleteAtEnd()
        else:
            prev = None 
            curr = self.head 
            count = 0
            while count < index:
                prev = curr
                curr = curr.next 
                count += 1
            prev.next = curr.next 
            self._size -= 1

    # Time: O(n) | Space: O(1)  — O(n) to find the node with the matching value
    def deleteByValue(self, value: Any) -> None:
        prev = None 
        curr = self.head 
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    self.deleteAtFirst()
                elif curr == self.tail:
                    self.deleteAtEnd()
                else:
                    prev.next = curr.next
                    self._size -= 1
                return
            prev = curr
            curr = curr.next
    

            


    


        


ll = LinkedList()
ll.append(78)
ll.append(3)
ll.append(9)
ll.prepend(10)
ll.insert(88,2)
for node in ll:
    print(node, end=" -> ")
print("None")

ll.deleteAtIndex(2)

for node in ll:
    print(node, end=" -> ")
print("None")

    
    