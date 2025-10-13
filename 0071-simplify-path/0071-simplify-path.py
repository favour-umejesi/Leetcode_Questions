class Solution:
    def simplifyPath(self, path: str) -> str:
        """PSEUDOCODE 
        -make an empty stack
        -split the string by "/"
        -add elements unto the stack
        -if the character is .. then pop an item from the stack
        -if the character is . do not add it to the stack
        -if / is the last character do not add to the stack
        
        """
        stack = []
        output = []
        path = path.split("/")

        for item in path:
            if item != "":
                output.append(item)

        for item in output:
            if item != "." and item != "..":
                stack.append(item)

            elif stack and item == "..":
                stack.pop()


        return "/" + "/".join(stack)


        