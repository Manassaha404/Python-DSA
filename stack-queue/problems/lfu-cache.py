# LFU Cache
# https://leetcode.com/problems/lfu-cache/description/ 

# Time Complexity  :
#   - get(key)        : O(1) — hash map lookup, node removal from current frequency DLL, and insertion into incremented frequency DLL
#   - put(key, value) : O(1) — hash map operations, evicting the least frequently/least recently used node, and insertion into frequency 1 DLL
# Space Complexity : O(capacity) — hash maps and doubly linked lists collectively store at most 'capacity' items
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

    def deleteNode(self, node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def preAppendNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def isEmpty(self):
        return self.size == 0


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        dll = DoublyLinkedList()
        self.fqTodll = {1: dll}
        self.keyToNode = {}
        self.keyTofq = {}
        self.lfc = 1

    def increseKeyFq(self, key):
        keyToNode = self.keyToNode
        keyTofq = self.keyTofq
        fqTodll = self.fqTodll
        lfc = self.lfc
        keyFq = keyTofq[key]
        fqDll = fqTodll[keyFq]
        node = keyToNode[key]
        fqDll.deleteNode(node)
        newFq = keyFq + 1
        if fqDll.isEmpty() and keyFq == lfc:
            self.lfc = newFq
        if newFq in fqTodll:
            newFqDll = fqTodll[newFq]
            newFqDll.preAppendNode(node)
            keyTofq[key] = newFq
        else:
            newFqDll = DoublyLinkedList()
            newFqDll.preAppendNode(node)
            keyTofq[key] = newFq
            fqTodll[newFq] = newFqDll

    def get(self, key: int) -> int:
        keyToNode = self.keyToNode
        keyTofq = self.keyTofq
        fqTodll = self.fqTodll
        lfc = self.lfc
        if key in keyToNode:
            node = keyToNode[key]
            self.increseKeyFq(key)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        keyToNode = self.keyToNode
        keyTofq = self.keyTofq
        fqTodll = self.fqTodll
        lfc = self.lfc
        if key in keyToNode:
            node = keyToNode[key]
            node.val = value
            self.increseKeyFq(key)
            return
        if self.size >= self.capacity:
            lfcDll = fqTodll[lfc]
            delNode = lfcDll.deleteFromBack()
            del keyToNode[delNode.key]
            del keyTofq[delNode.key]
            self.size -= 1
        dll = fqTodll[1]
        node = dll.preAppend(key, value)
        self.lfc = 1
        keyTofq[key] = 1
        keyToNode[key] = node
        self.size += 1

    # Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)