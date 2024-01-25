# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        ahead = head
        while n:
            ahead = ahead.next
            n-=1
        prev = None
        while ahead:
            prev = curr
            curr = curr.next
            ahead = ahead.next
        if prev: prev.next = curr.next

        return head if prev else head.next
        