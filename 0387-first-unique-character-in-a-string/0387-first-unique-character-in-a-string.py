from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        for i, value in enumerate(s):
            if freq[value] == 1:
                return i

        return -1

        