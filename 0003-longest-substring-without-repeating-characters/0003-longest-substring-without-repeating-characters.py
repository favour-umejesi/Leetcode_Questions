class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        currLen , left, longestLen = 0, 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                currLen -= 1
            seen.add(s[right])
            currLen += 1
            longestLen = max(longestLen, currLen)

        return longestLen
        