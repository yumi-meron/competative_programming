# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        newNode1 = ListNode()
        newNode2 = ListNode()
        curr1 = newNode1
        curr2 = newNode2
        curr = head

        while curr:
            if curr.val < x:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
                
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
            curr = curr.next
        curr1.next = newNode2.next
        return newNode1.next
                
               


        