"""
U - if ch # in string, once found, delete character before it, then check if what is left of the two strings is equal.
M - String, Stack
P - 1) Create two stacks for each of the strings
  - 2) Tranverse through each string
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for char in s:
            if char != "#":
                stackS.append(char)
            else:
                if stackS:
                    stackS.pop()

        for char in t:
            if char != "#":
                stackT.append(char)
            else:
                if stackT:
                    stackT.pop()


        return stackS == stackT