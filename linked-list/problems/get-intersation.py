class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time Complexity  : O(N + M) — where N and M are the lengths of list A and list B; each pointer traverses at most N + M nodes
# Space Complexity : O(1) — uses only two pointers with constant auxiliary space
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    temp1 = headA 
    temp2 = headB 
    # while temp1 and temp2:
    #     if temp1 == temp2:
    #         return temp1 
    #     temp1 = temp1.next 
    #     temp2 = temp2.next 
    #     if temp1 is None and temp2 is None:
    #         return None 
    #     if temp1 is None:
    #         temp1 = headB 
    #     if temp2 is None:
    #         temp2 = headA 
    # return None 
    while temp1 != temp2:
        temp1 = temp1.next if temp1 else headB
        temp2 = temp2.next if temp2 else headA
    return temp1