class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.k = k
        self.lenght = 0
        # self.lastNode = self.head
        

    def enQueue(self, value: int) -> bool:
        newNode = ListNode(value)
        if self.lenght < self.k:
            if self.head == None:
                self.head = newNode
                self.head.next = self.head
                self.head.prev = self.head
                
            else:
                newNode.prev = self.head.prev
                newNode.next = self.head
                self.head.prev.next = newNode
                self.head.prev = newNode
            self.lenght += 1
            return True
        else:
            return False
                      

    def deQueue(self) -> bool:
        
        if self.lenght > 1:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            
        elif self.lenght == 1:
            self.head = None
        else:
            return False
        self.lenght -= 1
        return True        
        

    def Front(self) -> int:
        return self.head.val if self.head else -1
        

    def Rear(self) -> int:
        if self.head is not None and self.head.prev is not None:
            return self.head.prev.val
        else:
            return -1
    

    def isEmpty(self) -> bool:
        return self.lenght == 0
                 

    def isFull(self) -> bool:
        return self.lenght == self.k
           
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()