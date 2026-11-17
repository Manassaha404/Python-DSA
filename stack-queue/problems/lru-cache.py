# LRU Cache
# https://leetcode.com/problems/lru-cache/description/ 

# Time Complexity  :
#   - get(key)        : O(1) — hash map lookup and doubly linked list node movement to head
#   - put(key, value) : O(1) — hash map insertion/update and doubly linked list prepend/eviction
# Space Complexity : O(capacity) — hash map and doubly linked list store at most 'capacity' key-node pairs
class Node:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def preAppend(self, key, val):
        new_node = Node(val, key, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        return new_node

    def deleteFromBack(self):
        if self.size == 0:
            return None
        delNode = self.tail.prev
        self.tail.prev = delNode.prev
        delNode.prev.next = self.tail
        delNode.next = None
        delNode.prev = None
        self.size -= 1
        return delNode

    def deleteNodeAndPreAppend(self, node):
        if node == self.head.next:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.keyToNode = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        keyToNode = self.keyToNode
        dll = self.dll
        if key in keyToNode:
            node = keyToNode[key]
            dll.deleteNodeAndPreAppend(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        keyToNode = self.keyToNode
        dll = self.dll
        capacity = self.capacity
        if key in keyToNode:
            node = keyToNode[key]
            node.val = value
            dll.deleteNodeAndPreAppend(node)
            return
        if len(dll) >= capacity:
            delNode = dll.deleteFromBack()
            del keyToNode[delNode.key]
        node = dll.preAppend(key, value)
        keyToNode[key] = node 