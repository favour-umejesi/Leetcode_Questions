class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        rev = list(num)
        left, right = 0, len(rev)-1

        while left < right:
            rev[left], rev[right] = rev[right], rev[left]
            left += 1
            right -= 1
        return "".join(rev) == num
        