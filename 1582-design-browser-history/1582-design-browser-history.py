class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.main_url = [homepage]

    def visit(self, url: str) -> None:
        self.main_url.append(url)
        self.history.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.main_url) > 1:
            remove = self.main_url.pop()
            self.history.append(remove)
            steps -= 1
        return self.main_url[-1]

    def forward(self, steps: int) -> str:
        while steps and self.history:
            add = self.history.pop()
            self.main_url.append(add)
            steps -= 1
        return self.main_url[-1]


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)