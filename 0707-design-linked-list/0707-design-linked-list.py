class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current == None:
                return -1
            else:
                current= current.next
        return current.val  if current else -1

        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node     
        
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        current = self.head
        for i in range(index-1):
            if not current:
                return
            current = current.next
         
        new_node = ListNode(val)
        new_node.next = current.next if current else None
        if current:
            current.next = new_node
        
                                    
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 :
            return
        elif index == 0:
            self.head = self.head.next if self.head else None
            return
       
        current = self.head
        for i in range(index-1):
            if not current:
                return
            current = current.next
            
        if current and current.next:
            current.next = current.next.next

                    
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)