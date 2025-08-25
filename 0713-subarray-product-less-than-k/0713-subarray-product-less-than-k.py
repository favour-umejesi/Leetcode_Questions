class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        U - Return the number of contigous subarrays in the array, that can give a product less than K
        M - Sliding window, Array
        P - left = product = length = 
          - for right in nums:
                product *= nums[right]

        - create an invalid window that would break once the product less than k
        - if the condition breaks, we divide the current product by the number leaving the window 
        - product *= nums
        """
        left, length = 0, 0
        product = 1
        if k <= 1:
            return 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            length += right-left+1

        return length
            
            
            


            

        