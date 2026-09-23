class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_set = set()
        left = ans = 0

        for right in range(len(s)):
            while s[right] in character_set:
                character_set.remove(s[left])
                left += 1

            character_set.add(s[right])
            ans = max(ans, right-left+1)

        return ans
