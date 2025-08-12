"""
U - Check if a string is the acronoym of words of in a list.
M - String, array
P - First we check the length of the list and string, if they are not equal, return False
  - create an empty string, then add the first letter of each word in the string and then compare with s, if they are equal we return True.
  - Another optimal solution will be to iterate through the string, and check the letters in it is equal to the first letters of the words in the string

"""
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        if len(s) != len(words):
            return False

        # t = ""

        # for word in words:
        #     t += word[0]

        # return s == t

        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False

        return True
        