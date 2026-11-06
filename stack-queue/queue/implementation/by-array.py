from typing import Any


class Queue:
    """
    A simple Linear Queue implementation using a fixed-size array
    (non-circular).
    """

    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        # Pre-allocate fixed-size array filled with None
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1

    # Time: O(1) | Space: O(1)
    def is_empty(self) -> bool:
        return self.front > self.rear

    # Time: O(1) | Space: O(1)
    def is_full(self) -> bool:
        return self.rear == self.capacity - 1

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        if self.is_empty():
            return 0
        return self.rear - self.front + 1

    # Time: O(1) | Space: O(1)
    def enqueue(self, value: Any) -> None:
        """Insert an element at the rear of the linear queue."""
        if self.is_full():
            raise OverflowError("Queue Overflow: Cannot enqueue to a full queue")
        self.rear += 1
        self.arr[self.rear] = value

    # Time: O(1) | Space: O(1)
    def dequeue(self) -> Any:
        """Remove and return the element at the front of the linear queue."""
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue")
        value = self.arr[self.front]
        self.arr[self.front] = None  # Clear reference
        self.front += 1

        # Reset pointers when queue becomes completely empty to reclaim space
        if self.front > self.rear:
            self.front = 0
            self.rear = -1

        return value

    # Time: O(1) | Space: O(1)
    def peek(self) -> Any:
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue Underflow: Queue is empty")
        return self.arr[self.front]

    # Time: O(n) | Space: O(n)
    def display(self) -> None:
        if self.is_empty():
            print("Queue: [Empty]")
            return
        elements = [str(self.arr[i]) for i in range(self.front, self.rear + 1)]
        print(f"Queue (Front -> Rear): {' -> '.join(elements)}")


# Example Usage

q = Queue(capacity=5)

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

print(f"Is full? {q.is_full()}")  # True
