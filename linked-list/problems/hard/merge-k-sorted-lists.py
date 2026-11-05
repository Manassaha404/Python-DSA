# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
from itertools import count
# Time Complexity  : O(N log k) — where N is the total number of nodes across all k lists, and k is the number of linked lists. Each insertion and extraction in the min-heap of size at most k takes O(log k) time.
# Space Complexity : O(k) — min-heap stores at most k nodes at any given time (one from each list).
def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    tie = count()
    nodes = []
    for i in range(len(lists)):
        if lists[i]:
            node = lists[i]
            heapq.heappush(nodes, [node.val, next(tie), node])
    dummy = ListNode()
    temp = dummy
    while len(nodes) != 0:
        [val, fn, node] = heapq.heappop(nodes)
        temp.next = node
        temp = temp.next
        if node.next:
            heapq.heappush(nodes, [node.next.val, next(tie), node.next])
    return dummy.next