class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0 #use to keep track of where the next (non-val) element should be placed

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i] # if it is not equal to val, replace the curr number with the number at position j, then move j, if not skip
                j += 1
        
        return j
        