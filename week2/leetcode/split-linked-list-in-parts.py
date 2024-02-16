# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        
        curr = head
        l = n//k
        rem = n%k
        ans = []

        for i in range(k):
            
            dummy = ListNode(0)
            sub = dummy
            if i < rem:
                for _ in range(l+1):
                    sub.next = ListNode(curr.val)
                    sub = sub.next
                    curr = curr.next
            else:
                for _ in range(l):
                    if curr:
                        sub.next = ListNode(curr.val)
                        sub = sub.next
                        curr = curr.next
               
            ans.append(dummy.next)

        return ans