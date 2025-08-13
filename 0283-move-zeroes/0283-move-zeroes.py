"""
U - Move zeroes to the end of the list
M - Array, Two Pointers
P - create a pointer to keep track of zeroes, set it to first index
  - if the current element is non zero, swap it with the previous element
  - increment the element that keeps track of zeroes to update the position for the next non-zero element
  - Continue iterating until all elements are processed, ensuring all non-zero elements are moved to the front of the array and zeros are pushed to the end.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
        