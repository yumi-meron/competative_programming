class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.current = self.home

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.next = node
        node.prev = self.current 
        self.current = node

        

    def back(self, steps: int) -> str:
        
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.url


    def forward(self, steps: int) -> str:
        
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)