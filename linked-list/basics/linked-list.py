from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.dummy: Node = Node(None)   # sentinel, sits before the first real node
        self.tail: Node = self.dummy    # points at dummy when the list is empty
        self._size = 0

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self._size

    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        cur = self.dummy.next
        while cur:
            yield cur.value
            cur = cur.next

    # Time: O(1) | Space: O(1)
    def prepend(self, value: Any) -> None:
        node = Node(value, self.dummy.next)
        self.dummy.next = node
        if self.tail is self.dummy:     # list was empty
            self.tail = node
        self._size += 1

    # Time: O(1) | Space: O(1)  — O(1) because we maintain a tail pointer
    def append(self, value: Any) -> None:
        node = Node(value)
        self.tail.next = node           # works for empty list too (tail is dummy)
        self.tail = node
        self._size += 1

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def insert(self, value: Any, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if index == self._size - 1:     # kept from your original: appends at the end
            self.append(value)
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = Node(value, prev.next)
        self._size += 1

    # Time: O(1) | Space: O(1)
    def deleteAtFirst(self) -> None:
        if self._size == 0:
            return
        first = self.dummy.next
        self.dummy.next = first.next
        if first is self.tail:          # removed the only node
            self.tail = self.dummy
        first.next = None
        self._size -= 1

    # Time: O(n) | Space: O(1)  — O(n) to reach the second-to-last node
    def deleteAtEnd(self) -> None:
        if self._size == 0:
            return
        prev = self.dummy
        while prev.next is not self.tail:
            prev = prev.next
        prev.next = None
        self.tail = prev                # becomes dummy if the list is now empty
        self._size -= 1

    # Time: O(n) | Space: O(1)  — O(n) to traverse to the given index
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        curr = prev.next
        prev.next = curr.next
        if curr is self.tail:
            self.tail = prev
        curr.next = None
        self._size -= 1

    # Time: O(n) | Space: O(1)  — O(n) to find the node with the matching value
    def deleteByValue(self, value: Any) -> None:
        prev = self.dummy
        while prev.next is not None:
            curr = prev.next
            if curr.value == value:
                prev.next = curr.next
                if curr is self.tail:
                    self.tail = prev
                curr.next = None
                self._size -= 1
                return
            prev = curr


ll = LinkedList()
ll.append(78)
ll.append(3)
ll.append(9)
ll.prepend(10)
ll.insert(88, 2)
for node in ll:
    print(node, end=" -> ")
print("None")

ll.deleteAtIndex(2)

for node in ll:
    print(node, end=" -> ")
print("None")