from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top: Optional[Node] = None # Top pointer points to the head of the linked list (most recently added node)
        self._size = 0

    # Time: O(1) | Space: O(1)
    def is_empty(self) -> bool:
        return self.top is None

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self._size

    # Time: O(1) | Space: O(1)
    def push(self, value: Any) -> None:
        # Insert a new element at the top of the stack (head of linked list).
        new_node = Node(value, next=self.top)
        self.top = new_node
        self._size += 1

    # Time: O(1) | Space: O(1)
    def pop(self) -> Any:
        # Remove and return the topmost element (head of linked list).
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped_value

    # Time: O(1) | Space: O(1)
    def peek(self) -> Any:
        # Return the topmost element without removing it.
        if self.is_empty():
            raise IndexError("Stack Underflow: Stack is empty")
        return self.top.value

    # Time: O(n) | Space: O(1)
    def __iter__(self) -> Iterator[Any]:
        # Iterate through the stack from Top to Bottom.
        curr = self.top
        while curr:
            yield curr.value
            curr = curr.next

    # Time: O(n) | Space: O(n)
    def display(self) -> None:
        if self.is_empty():
            print("Stack: [Empty]")
            return
        elements = [str(val) for val in self]
        print(f"Stack (Top -> Bottom): {' -> '.join(elements)}")


# Example Usage 

st = Stack()

print(f"Is empty? {st.is_empty()}")  # True

st.push(10)
st.push(20)
st.push(30)
st.display()  # Stack (Top -> Bottom): 30 -> 20 -> 10

print(f"Top element (peek): {st.peek()}")  # 30
print(f"Size of stack: {len(st)}")         # 3

print(f"Popped: {st.pop()}")  # 30
st.display()  # Stack (Top -> Bottom): 20 -> 10

st.push(40)
st.push(50)
st.display()  # Stack (Top -> Bottom): 50 -> 40 -> 20 -> 10
print(f"Size of stack: {len(st)}")         # 4

