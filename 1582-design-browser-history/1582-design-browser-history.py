class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [] #store visited tabs
        self.main_url = [homepage] #store tabs we are visiting

    def visit(self, url: str) -> None:
        self.main_url.append(url) #store tabs we are currently on
        self.history.clear() #clear history when visiting a new tab

    def back(self, steps: int) -> str:
        while steps and len(self.main_url) > 1: #checks if the homepage is still intact
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