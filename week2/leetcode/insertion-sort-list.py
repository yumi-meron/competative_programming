# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode(head.val)
        def insertAtBegin(value):
            nonlocal sortedList
            newNode = ListNode(value)
            newNode.next = sortedList
            sortedList = newNode

        def insertAtMiddle(value, current):
            newNode = ListNode(value)
            dummy = current.next
            current.next = newNode
            newNode.next = dummy

        def search(value):
            curr1, prev = sortedList, None
            while curr1 and curr1.val < value:
                prev = curr1
                curr1 = curr1.next
            return prev

        
        curr1 = sortedList
        curr = head.next
        while curr:
            prev = search(curr.val)
            if not prev: 
                insertAtBegin(curr.val)
            else:
                insertAtMiddle(curr.val, prev)
            curr = curr.next
                
            
        return sortedList

        