class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        create two hashmaps
        each hashmap storing index to the characters, if the resulting hashmaps don't have the same 
        """
        if len(s) != len(t):
            return False
        d_s = {}
        d_t = {}

        for i in range(len(s)):
            if s[i] not in d_s:
                d_s[s[i]] = i

            if t[i] not in d_t:
                d_t[t[i]] = i


            if d_s[s[i]] != d_t[t[i]]:
                return False

        return True