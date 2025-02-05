# L.1790, Check if One String Swap Can Make Strings Equal.
"""
U - The question wants us to check if a single swap in a string (s1 or s2) can make it equal to the other.
M - Strings, Hashmap, Two Pointers, Counting
P - Use two dictionaries to store the frequency of each letter in the strings, then check if the two dictionaries are equal to each other.
- To meet the condition that states at most swap exactly one of the strings, we set a variable count, then we use two pointers to check if the first letter of a string is equal to the first letter of the other string, if not increment count (the number of times the letters are not equal to each other), if we need to swap elements in the string more than one time, then it is false.if count is greater than 2, we return false.

I - Implement (Code)
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        dict_1 = {}
        dict_2 = {}

        for letter in s1:
            if letter in dict_1:
                dict_1[letter] += 1
            else:
                dict_1[letter] = 1
        
        for word in s2:
            if word in dict_2:
                dict_2[word] += 1
            else:
                dict_2[word] = 1

        i, j = 0,0
        count = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                count += 1
                i += 1
                j += 1
        
        if count > 2:
            return False
            
        return dict_1 == dict_2
        
"""
R - Review
Before making use of two-pointers, the code failed for this test case input: s1 = "bank", s2 = "knab". Because you would need to swap letters in s2 to make it equal to s1 or vice versa, which is not what we want. So to address this, we make use of two pointers and counting method to make sure swap will occur at most once.

E - Evaluate
The function "areAlmostEqual" checks if two strings s1 and s2 can be made equal by swapping at most one pair of characters in one of the strings. This implies that:
-The two strings must be of equal length (otherwise, they cannot be made equal by swapping).
-The number of mismatched characters between the two strings must be 0 or 2 (for a single swap to fix the mismatch).

Updated Time Complexity:
Dictionary Construction:
- Iterating over s1 to populate dict_1 takes O(n) time.
- Iterating over s2 to populate dict_2 takes O(n) time.

Total time for dictionary construction: O(n)+O(n)=O(n).

Character Comparison:
-The while loop compares characters of s1 and s2 at the same indices. Since the strings are of equal length, this loop runs exactly n times.
Time for character comparison: O(n).

Dictionary Comparison:
- Comparing two dictionaries (dict_1 and dict_2) takes O(n) time in the worst case, as there can be up to n unique characters.

Overall Time Complexity:
- The dominant operations are the dictionary construction, character comparison, and dictionary comparison, all of which are O(n).

Total time complexity: O(n).

Space Complexity:
Dictionary Storage:
- dict_1 stores up to n unique characters from s1.
- dict_2 stores up to n unique characters from s2.

Total space for dictionaries: O(n)+O(n)=O(n).

Other Variables:
- The variables i, j, and count use constant space, O(1).

Overall Space Complexity:
- The dominant space usage is from the dictionaries, so the total space complexity is O(n).

Final Answer (Under Equal Length Assumption):
Time Complexity: O(n)
Space Complexity: O(n)

Where n is the length of the input strings s1 and s2.

"""
