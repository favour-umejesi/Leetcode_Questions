class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Given roman numerals, convert it to integer
        Plan:
        - Create a dictionary containing the roman numerals, mapped to integers
        - looping through the string, we check if the first roman integer we encounter is less than the one after it
            - if so, we substract its value from total
            - else, we keep adding
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        total += roman[s[-1]]
        return total
