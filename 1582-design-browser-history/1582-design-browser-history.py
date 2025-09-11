class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = [homepage]
        

    def visit(self, url: str) -> None:
        self.future.append(url)
        self.history.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.future) > 1:
            remove = self.future.pop()
            self.history.append(remove)
            steps -= 1
        return self.future[-1]

    def forward(self, steps: int) -> str:
        while steps and self.history:
            add = self.history.pop()
            self.future.append(add)
            steps -= 1
        return self.future[-1]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)