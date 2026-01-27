class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        num = list(n)

        left, right = 0, len(num)-1

        while left < right:
            num[left], num[right] = num[right], num[left]

            left += 1
            right -= 1

        return "".join(num) == n
        