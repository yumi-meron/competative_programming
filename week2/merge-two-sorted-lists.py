# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = ListNode()
        newcurr = head1
        curr1, curr2 = list1, list2
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                newcurr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                newcurr.next = ListNode(curr2.val)
                curr2 = curr2.next
            newcurr = newcurr.next
        if curr1: newcurr.next = curr1
        if curr2: newcurr.next = curr2

        return head1.next


        