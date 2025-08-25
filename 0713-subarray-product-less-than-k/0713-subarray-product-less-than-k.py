class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Understand - Return a number of subarrays that will give a product less than k
        Match - Array, Sliding Window
        Plan - Initialize the left and right pointer which starts at index zero, Count, to keep track of subarrays
             - Variable product to keep track of the total product of the subarrays
             - we also have to think of a situation of if k is less than or equal to 1, then we return 0
             - we start by building our window
             - we set an invalid window of when product is greater than K
                - where we use floor division to reduce the product and also increment the left pointer to shrink our window
             - If the condition breaks, we add the length of the subarrays to count
        """
        left, product, count = 0, 1, 0
        if k <= 1:
            return 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += (right - left + 1)
        return count