# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# • Open brackets must be closed by the same type of brackets.
# • Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching = []
        brackets = {'(':')','[':']','{':'}'}
        for element in s:
            if element in brackets:
                matching += brackets[element]
            else:
                if matching == [] or matching.pop() != element:                    
                    return False
        if matching != []:
            return False
        return True
                
s = "([)]"
print(Solution().isValid(s))