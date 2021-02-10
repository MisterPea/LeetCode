class Solution(object):
    
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        total = []
        num1_length = len(num1)
        num2_length = len(num2)
        diff = abs(num1_length - num2_length)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        if num1_length > num2_length:
            num2 += "0" * diff
        elif num2_length > num1_length:
            num1 += "0" * diff

        for i in range(0, max(num1_length,num2_length)):
            current_int = int(num1[i]) + int(num2[i]) + carry
            carry = 0
            if current_int > 9:
                carry = 1
                current_int = current_int % 10
            total += [str(current_int)]
        if carry != 0:
            total += [str(carry)]
        total.reverse()
        return ''.join(total)
        
		


num1 = '6789'
num2 = '123'
s = Solution()
print(s.addStrings(num1, num2))
        

