# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        curr_list = []
        rev_num = 0
        org_num = x
        while x != 0:
            curr_list += [x % 10]
            x = x // 10
        
        length = len(curr_list)
        for i in range(0, length):
            rev_num += curr_list[length - i - 1] * 10 ** i
        return org_num - rev_num == 0
            

        


x = 1221
s = Solution()
print(s.isPalindrome(x))