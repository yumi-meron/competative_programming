# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddhead = ListNode()
        evenhead = ListNode()
        curr,curr1,curr2 = head, oddhead, evenhead
        while curr and curr.next:
            dummy = curr.next
            curr1.next = curr
            curr2.next = dummy
            curr = dummy.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr: 
            curr1.next = curr
            curr1 = curr1.next

        curr1.next = evenhead.next
        curr2.next = None
        return oddhead.next
        
        