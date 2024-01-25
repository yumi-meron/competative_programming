# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            dummy = slow.next
            slow.next = prev
            prev = slow
            slow = dummy
        
        left = head
        right = prev
        while left and right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True
        # if not head:
        #     return True

        # newhead = ListNode(head.val)
        # curr = head.next
        # curr1 = newhead
    
        # while curr:
        #     curr1.next = ListNode(curr.val)
        #     curr1 = curr1.next
        #     curr = curr.next
        
        # prev, ahead = None, newhead
        # while ahead:
        #     dummy = ahead.next
        #     ahead.next = prev
        #     prev = ahead
        #     ahead = dummy
        # head2 = prev

        # current1 = head
        # current2 = head2
        # while current1:
        #     if current1.val != current2.val:
        #         return False
        #     current1 = current1.next
        #     current2 = current2.next

        # return True
        