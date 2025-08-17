"""
U - if ch # in string, once found, delete character before it, then check if what is left of the two strings is equal.
M - String, Stack
P - 1) Create two stacks for each of the strings
  - 2) Tranverse through each string
        - check if char is != "#":
        - If so, append char to stack
        - else, we check if stack is not empty and pop last element
    3) After repeating for second string, compare the two stacks
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def helper(word):
            stack = []
            for char in word:
                if char != "#":
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return stack

        return helper(s) == helper(t)

        
        # stackS = []
        # stackT = []
        
        # for char in s:
        #     if char != "#":
        #         stackS.append(char)
        #     else:
        #         if stackS:
        #             stackS.pop()

        # for char in t:
        #     if char != "#":
        #         stackT.append(char)
        #     else:
        #         if stackT:
        #             stackT.pop()


        # return stackS == stackT