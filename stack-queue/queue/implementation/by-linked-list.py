from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class Queue:
    """
    A simple Linear Queue implementation using a Singly Linked List
    (non-circular, with front and rear pointers).
    """

    def __init__(self):
        # Front points to the head (oldest element, exit point)
        self.front: Optional[Node] = None
        # Rear points to the tail (newest element, entry point)
        self.rear: Optional[Node] = None
        self._size = 0

    # Time: O(1) | Space: O(1)
    def is_empty(self) -> bool:
        return self.front is None

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self._size

    # Time: O(1) | Space: O(1)
    def enqueue(self, value: Any) -> None:
        """Insert an element at the rear of the queue."""
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    # Time: O(1) | Space: O(1)
    def dequeue(self) -> Any:
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        # If queue became empty, reset rear to None as well
        if self.front is None:
            self.rear = None
        self._size -= 1
        return value

    # Time: O(1) | Space: O(1)
    def peek(self) -> Any:
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue Underflow: Queue is empty")
        return self.front.value

    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        """Iterate through the queue from Front to Rear."""
        curr = self.front
        while curr:
            yield curr.value
            curr = curr.next

    # Time: O(n) | Space: O(n)
    def display(self) -> None:
        if self.is_empty():
            print("Queue: [Empty]")
            return
        elements = [str(val) for val in self]
        print(f"Queue (Front -> Rear): {' -> '.join(elements)}")


# Example Usage 

q = Queue()

print(f"Is empty? {q.is_empty()}")  # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  # Queue (Front -> Rear): 10 -> 20 -> 30

print(f"Front element (peek): {q.peek()}")  # 10
print(f"Size of queue: {len(q)}")           # 3

print(f"Dequeued: {q.dequeue()}")  # 10
q.display()  # Queue (Front -> Rear): 20 -> 30

q.enqueue(40)
q.enqueue(50)
q.display()  # Queue (Front -> Rear): 20 -> 30 -> 40 -> 50
print(f"Size of queue: {len(q)}")           # 4

