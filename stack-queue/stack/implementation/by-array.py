from typing import Any


class Stack:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity    # Pre-allocate fixed-size array filled with None
        self.arr = [None] * capacity
        self.top = -1               # Points to the index of the topmost element (-1 means stack is empty)

    # Time: O(1) | Space: O(1)
    def is_empty(self) -> bool:
        return self.top == -1

    # Time: O(1) | Space: O(1)
    def is_full(self) -> bool:
        return self.top == self.capacity - 1

    # Time: O(1) | Space: O(1)
    def __len__(self) -> int:
        return self.top + 1

    # Time: O(1) | Space: O(1)
    def push(self, value: Any) -> None:
        if self.is_full():
            raise OverflowError("Stack Overflow: Cannot push to a full stack")
        self.top += 1
        self.arr[self.top] = value

    # Time: O(1) | Space: O(1)
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")
        value = self.arr[self.top]
        self.arr[self.top] = None  # Clear reference
        self.top -= 1
        return value

    # Time: O(1) | Space: O(1)
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack Underflow: Stack is empty")
        return self.arr[self.top]

    # Time: O(n) | Space: O(n)
    def display(self) -> None:
        if self.is_empty():
            print("Stack: [Empty]")
            return
        elements = [str(self.arr[i]) for i in range(self.top, -1, -1)]
        print(f"Stack (Top -> Bottom): {' -> '.join(elements)}")




st = Stack(capacity=5)

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
st.push(60)
st.display()  # Full capacity reached: 5 items

print(f"Is full? {st.is_full()}")  # True

