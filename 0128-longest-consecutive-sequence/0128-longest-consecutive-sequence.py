class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in numSet:
            #Check if it is the start of a sequence
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet: #check current number
                    length += 1
                #if the condition breaks we the max length of the sequence
                longest = max(length, longest)

        return longest