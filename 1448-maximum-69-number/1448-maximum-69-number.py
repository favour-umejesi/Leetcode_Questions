class Solution:
    def maximum69Number (self, num: int) -> int:

        """
        U - Giving a digit that contains only "6's" and "9's", return the maximum number you can get by flipping a digit
        M - Number
        P - 1) Convert digit to string and list
            2) Changing the first 6 we encounter to 9, gives us the maximun number
            3) using the join function, convert list to  a string and then to an int, return answer
        """

        nums = list(str(num))

        for i in range(len(nums)):
            if nums[i] == "6":
                nums[i] = "9"
                break
        
        return int("".join(nums))
        