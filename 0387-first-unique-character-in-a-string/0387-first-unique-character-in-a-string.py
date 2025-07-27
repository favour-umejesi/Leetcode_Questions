class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for c in s:
            seen[c] = 1 + seen.get(c, 0)

        for i, v in enumerate(s):
            if seen[v] == 1:
                return i

        return -1 
        