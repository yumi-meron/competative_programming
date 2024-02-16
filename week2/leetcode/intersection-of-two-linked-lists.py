# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lst1 = set()
        curr1 = headA
        while curr1:
            lst1.add(curr1)
            curr1 = curr1.next
        
        curr2 = headB
        while curr2:
            if curr2 in lst1:
                return curr2
            curr2 = curr2.next
        
        return None