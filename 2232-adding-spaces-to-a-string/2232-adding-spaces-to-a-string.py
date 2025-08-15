"""
U - given a list of numbers and a string, the numbers in the list are spaces to add to the string.
M - String, List
P - Initialize a new string to build the result incrementally
  - Initialize a variable, previous, to keep track of the starting index of the current substring in the input string s.
  - Iterate through the spaces list
  - Using list slicing, append the substring starting from prev-num, followed by a space
  - Then update previous to num
  - Append the remaining part of the string
  - After the loop, the remaining part of the string from the last index in spaces to the end of s (i.e., s[previous:]) is added to the new_string
  - Return the Result
"""
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_string = ""
        r = 0

        for num in spaces:
            new_string += s[r:num] + " "
            r = num

        new_string += s[num:]
        return new_string


        
        