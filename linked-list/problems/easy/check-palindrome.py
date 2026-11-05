# Palindrome Linked List 
# https://leetcode.com/problems/palindrome-linked-list/description/ 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def isPalindrome(head: ListNode | None) -> bool:
        # In-place Reverse Approach (commented out):
        # Time Complexity  : O(n) — find middle O(n) + reverse second half O(n) + compare O(n)
        # Space Complexity : O(1) — reversal done in place with a constant number of pointers
        # def findMiddle(head):
        #     if head is None:
        #         return head 
        #     slow = head 
        #     fast = head 
        #     while fast.next and fast.next.next:
        #         slow = slow.next if slow else None 
        #         fast = fast.next.next 
        #     return slow 
        # mid = findMiddle(head) 
        # def reverseList(head: ListNode | None) -> ListNode | None:
        #     if head is None:
        #         return None 
        #     prev = None 
        #     curr = head 
        #     while curr:
        #         temp = curr.next 
        #         curr.next = prev 
        #         prev = curr 
        #         curr = temp 
        #     return prev
        # newHead = reverseList(mid.next) 
        # temp1 = newHead 
        # temp2 = head
        # while temp1:
        #     if temp1.val != temp2.val:
        #         return False 
        #     else:
        #         temp1 = temp1.next 
        #         temp2 = temp2.next 
        # reverseList(newHead)
        # return True
        # Stack-based Approach (active):
        # Time Complexity  : O(n) — one pass to push first half onto stack + one pass to compare second half
        # Space Complexity : O(n/2) = O(n) — stack stores values of the first half of the list
        slow = head 
        fast = head 
        stack = [] 
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next if slow else None 
            fast = fast.next.next
        if fast:
            slow = slow.next 
        while slow:
            el = stack.pop()
            if el != slow.val:
                return False 
            else:
                slow = slow.next 
        return True