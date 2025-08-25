class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
    Given an array, find the maximum product of three numbers
    We can't use the sliding window approach, because we are asked for product of any three numbers not a subsequence.
    The maximum product of 3 numbers will either be:
	    - The product of the 3 largest numbers
	    - The product of the 2 smallest numbers (possibly negative) and the largest number

        """
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

        