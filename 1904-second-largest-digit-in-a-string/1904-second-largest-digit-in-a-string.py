class Solution:
    def secondHighest(self, s: str) -> int:
        arr = [int(char) for char in s if char.isdigit()]

        largest, second = -1, -1

        for num in arr:
            if num > largest:
                second = largest
                largest = num

            if num < largest and num > second:
                second = num


        return second
        