class Solution:
    def makeFancyString(self, s: str) -> str:

        stack = []
        count = 1

        for letter in s:
            if stack and stack[-1] == letter:
                count += 1
            if stack and stack[-1] != letter:
                count = 1

        
            if count >= 3:
                continue
            
            else:
                stack.append(letter)

        return "".join(stack)


        