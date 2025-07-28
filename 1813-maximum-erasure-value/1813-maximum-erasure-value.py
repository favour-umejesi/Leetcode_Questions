class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()

        left = currSum = maxSum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currSum -= nums[left]
                left += 1

            seen.add(nums[right])
            currSum += nums[right]

            maxSum = max(maxSum, currSum)
        return maxSum
        