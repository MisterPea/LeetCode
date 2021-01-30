# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        vowels = ['a','e','i','o','u']
        for letter in s:
            if letter not in vowels:
                new_string += letter
        return new_string

s = "leetcodeisacommunityforcoders"
Solution()
print(Solution().removeVowels(s))