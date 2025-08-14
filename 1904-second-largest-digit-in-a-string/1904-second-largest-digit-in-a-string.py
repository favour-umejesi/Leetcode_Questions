"""
U - Find the second largest digit in a string
M - String
P - 1) Create a list containing digits from the string
  - 2) Set two variables, one as the largest element in the list, and the other as second largest element, set to -1, to handle a case of it is does not exist.
  - 3) Iterate through the list, if num is larger than largestNum, set secondLargest to LargestNum, and LargestNum to num.
  - 4) If num is less than LargestNum, and greater than SecondLargest, then sent secondLargest to num.
  - 5) Return secondLargest
"""
class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [int(char) for char in s if char.isdigit()]

        largest = -1
        secondLargest = -1

        for num in nums:
            if num > largest:
                secondLargest = largest
                largest = num

            if num < largest and num > secondLargest:
                secondLargest = num

        return secondLargest
        