"""
U- Return a list containing groups of words that are anagrams (identical) of each other
M- HashMap, Array
P- For this optimized solution, rather than sort the keys, we create an array of length 26, number of alphabets, and we use the ASCII values to decide index numbers. We subract the ASCII value of "a" from ASCII value of all characters, that's because ASCII value of a "a" is the smallest from "a" to "z". ASCII value of "a" is 97, ASCII value of "z" is "122"
- We can either import a default dictionary, or create an empty dictionary
- Iterate through the words, then set count to an array of length 26 with zeroes occupying it.
- Using the ASCII values of the letters, we use it to get the index of each character, and update its frequency in the list.
- We then make the array count our key, and a tuple because keys are immutable.
- we the check if the key is in the dictionary, if it is we append the word to values which is made up of a list, else we add the key to the dictionary, and a list containing the word as its value.
- Then we return a list of the dictionary values
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_dict[key].append(word)

        return list(anagram_dict.values())

        