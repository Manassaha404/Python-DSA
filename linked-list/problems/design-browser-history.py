# Design Browser History
# https://leetcode.com/problems/design-browser-history/description/ 
class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.prev = prev
# Time Complexity  : 
#   - __init__() : O(1)
#   - visit()    : O(1)
#   - back()     : O(steps) — at most min(steps, len) steps backward
#   - forward()  : O(steps) — at most min(steps, len) steps forward
# Space Complexity : O(N) — where N is the total number of URLs stored in the doubly linked list
class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = Node(homepage)
        self.head = new_node
        self.tail = new_node


    def visit(self, url: str) -> None:
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(url, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def back(self, steps: int) -> str:
        count = 0
        temp = self.tail
        while count != steps and temp.prev:
            temp = temp.prev
            count += 1
        self.tail = temp
        return self.tail.value


    def forward(self, steps: int) -> str:
        count = 0
        temp = self.tail
        while count != steps and temp.next:
            temp = temp.next
            count += 1
        self.tail = temp
        return self.tail.value




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)