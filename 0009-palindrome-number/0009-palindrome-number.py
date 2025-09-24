class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        rev = num[::-1]

        # x = str(x)
        # rev = x[::-1]
        return num == rev
        