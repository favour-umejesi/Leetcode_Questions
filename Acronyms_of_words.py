#Given an array of strings words and a string s, determine if s is an acronym of words.
#The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].
#Return true if s is an acronym of words, and false otherwise.

#Naive Approach 
class Solution:
  def isAcronym(self, words: List[str], s:str) -> bool: 
    if len(words) != len(s):
      return False
      first_letters = ""
    for word in words:
      first_letters += word[0]

	return first_letters == s

#Expected Approach

class Solution:
	def isAcronym(self, words: List[str], s:str) -> bool:
		if len(words) != len(s):
			return False
		else:
			for i in range(len(s)): #Iterate through each character in the acronym string
				if s[i] != words[i][0]: #Check if the character in the acronym string matches the first letter of the corresponding words
					return False
		return True
					
					


      

