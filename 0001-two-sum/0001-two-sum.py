class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in seen:
                return [i, seen[complement]]
            else:
                seen[n] = i


        