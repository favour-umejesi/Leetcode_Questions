class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = count = 0
        total = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):
            total *= nums[right]

            while total >= k:
                total //= nums[left]
                left += 1

            count += right - left + 1

        return count



        