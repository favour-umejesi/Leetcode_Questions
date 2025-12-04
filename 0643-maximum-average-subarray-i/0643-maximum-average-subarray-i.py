class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        maximum average of the numbers equal to k in the array
        start by building the first window and storing the average of the first k,
        """
        curr = 0
        max_avg = 0

        for i in range(k):
            curr += nums[i]

        max_avg = curr / k

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]

            max_avg = max(max_avg, curr/k)

        return max_avg