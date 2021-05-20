# Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = False
        while a != "" or b != "":
          test_a = "0"
          test_b = "0"
          if a != "":
            test_a = a[-1]
            a = a[:-1]
          if b != "":
            test_b = b[-1]
            b = b[:-1]

          both = test_a + test_b

          if both == "11" and carry == False:
            carry = True
            result += "0"
          elif both == "11" and carry == True:
            result += "1"
          elif (both == "01" or both == "10") and carry == True:
            result += "0"
          elif (both == "01" or both == "10") and carry == False:
            result += "1"
          elif both == "00" and carry == True:
            result += "1"
            carry = False
          elif both == "00" and carry == False: 
            result += "0"
        if carry == True:
          result += "1"
        return result[::-1]

a = "1011"
b = "1010"
s = Solution()
print(s.addBinary(a, b))