class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        -first we build the sum of the first k window
        - find the average
        - start building the other window from index of the window

        """
        ans = total = avg = 0

        for i in range(k):
            total += nums[i]

        avg = total/k

        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]

            avg = max(avg, total/k)

        return avg

        