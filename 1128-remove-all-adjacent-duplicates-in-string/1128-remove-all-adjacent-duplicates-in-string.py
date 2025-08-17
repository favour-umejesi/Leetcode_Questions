class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Create an empty stack
        Traverse through the string
        Check if stack is not empty and current character not equal to last 
        element in the stack
        if it is, pop last element, else append char 
        """

        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
        