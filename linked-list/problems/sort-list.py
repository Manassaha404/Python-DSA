# Sort List
# https://leetcode.com/problems/sort-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity  : O(N log N) — where N is the number of nodes; O(N) to traverse and store values, O(N log N) to sort the array, and O(N) to write back values (commented Merge Sort approach is also O(N log N))
# Space Complexity : O(N) — auxiliary array of size N to store node values (commented Merge Sort approach takes O(log N) recursion stack space)
def sortList(head: ListNode | None) -> ListNode | None:
    # def middleOfLL(node: ListNode):
    #     if node is None:
    #         return node
    #     fast = node
    #     slow = node
    #     while fast.next and fast.next.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
    # def mergeTwoSortedLL(node1, node2):
    #     temp1 = node1
    #     temp2 = node2
    #     dummy = ListNode()
    #     curr = dummy
    #     while temp1 and temp2:
    #         if temp2.val < temp1.val:
    #             curr.next = temp2
    #             temp2 = temp2.next
    #         else:
    #             curr.next = temp1
    #             temp1 = temp1.next
    #         curr = curr.next
    #     if temp1:
    #         curr.next = temp1
    #     if temp2:
    #         curr.next = temp2
    #     return dummy.next
    # def helper(node):
    #     if not node or node.next is None:
    #         return node
    #     middle = middleOfLL(node)
    #     leftHead = node
    #     rightHead = middle.next
    #     middle.next = None
    #     left = helper(leftHead)
    #     right = helper(rightHead)
    #     return mergeTwoSortedLL(left, right)
    # return helper(head)
    arr = []
    temp = head
    while temp:
        arr.append(temp.val)
        temp = temp.next
    arr = sorted(arr)
    temp = head
    for i in arr:
        temp.val = i
        temp = temp.next
    return head