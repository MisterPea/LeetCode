# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            print("rev:",rev_num, "x:",x)
            x = x // 10
        return x == rev_num or x == rev_num//10
        
# This solution:
# If x is negative or x mod 10 is 0 and x is not 0 then return False
# So, x being the original number will be bigger than rev_num until the halfway point.
# Once at the halfway point we see if current x is equal to rev_number.
# If not we see if the number length is even by floor division by 10.

            

        


x = 1221
s = Solution()
print(s.isPalindrome(x))