# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #Optimal Approach
        if not headA or not headB:
            return None
            
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l2

        # #Brute force approach
        # seen = set()
        # current = headA

        # # Add all values from headA to the set
        # while current:
        #     seen.add(current)
        #     current = current.next

        # # Check for first common value in headB
        # curr = headB
        # while curr:
        #     if curr in seen:
        #         return curr
        #     curr = curr.next

        # return None  