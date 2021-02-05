# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2 ** 31, 2 ** 31 - 1], then return 0.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum_list = []
        append = 1
        list_sum = 0
        if x < 0:
            append = -1
        x = abs(x)
        while x != 0:
            sum_list += [x % 10]
            x = x // 10
        length = len(sum_list)
        for i in range(0, length):
            list_sum += sum_list[length - i - 1] * 10 ** i
        
        if -2 ** 31 <= (list_sum * append) <= 2 ** 31 -1:
             return list_sum * append
        return 0



x = 184467
s = Solution()
print(s.reverse(x))