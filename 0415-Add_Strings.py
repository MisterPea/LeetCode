class Solution(object):
    
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        total = []
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        while index1 > -1 or index2 > -1:
            int_num1 = 0
            int_num2 = 0

            if index1 >= 0:
                int_num1 = int(num1[index1])
            if index2 >= 0:
                int_num2 = int(num2[index2])
            int_sum = int_num1 + int_num2 + carry
            carry = 0
                    
            if int_sum > 9:
                carry += 1
                int_sum = int_sum % 10
            total += [str(int_sum)]
            index1 -= 1
            index2 -= 1
            
        if carry != 0:
            total += [str(carry)]
        total.reverse()
        return ''.join(total)
		


num1 = '9999'
num2 = '0'
s = Solution()
print(s.addStrings(num1, num2))
        

