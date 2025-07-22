class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        U- if letter in string frequency is greater than 2, delete other occurences of it making sure we only have the minimum possible number of
        characters, not > 2
        Plan:
        keep count, two pointers, set one to 0, the other to 1
        create an empty string to keep characters that fall under the condition
        if l == r, increase count, else sent frequency to 1
        if count > 2, continue to skip element after 2 then add to the list, return list
        """
        res = ""
        l, r, c = 0, 1, 0

        for r in range(len(s)):
            if s[l] == s[r]:
                c += 1
            else:
                c = 1
            l = r
        
            if c > 2:
                continue
            
            res += s[l]
        
        return res

        