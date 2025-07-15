# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        #Brute force approach
        seen = set()
        current = headA

        # Add all values from headA to the set
        while current:
            seen.add(current)
            current = current.next

        # Check for first common value in headB
        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next

        return None  