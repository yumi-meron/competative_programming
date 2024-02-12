# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        last = None
        leftNode = None
        
        n = 1
        
        
        while curr:
            if n == left-1:
                prev = curr
            elif n == left:
                leftNode = curr
                pre = None
                while curr and n <= right:
                    if n == right: last = curr
                    dummy = curr.next
                    curr.next = pre
                    pre = curr
                    curr = dummy
                    n+=1
                
                leftNode.next = curr
                break    
            n+=1
            curr = curr.next

        if prev: prev.next = last
        else: head = last       

        return head



        
        
        
        
       