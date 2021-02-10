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
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(0, max(num1_length,num2_length)):
            if i > num1_length - 1:
                int1 = 0
            else:
                int1 = int(num1[i])
            
            if i > num2_length - 1:
                int2 = 0
            else:
                int2 = int(num2[i])

            current_int = int1 + int2 + carry

            carry = 0

            if current_int > 9:
                carry = 1
                current_int = current_int % 10
            total += [str(current_int)]
        if carry != 0:
            total += [str(carry)]
        return ''.join(total)[::-1]
        
		


num1 = '0'
num2 = '999999'
s = Solution()
print(s.addStrings(num1, num2))
        

