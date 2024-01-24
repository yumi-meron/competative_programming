# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        curr = head.next
        while curr:
            while curr and prev.val == curr.val:
                curr = curr.next
            prev.next = curr
            if not curr:
                break
            curr = curr.next
            prev = prev.next
            
        return head
        