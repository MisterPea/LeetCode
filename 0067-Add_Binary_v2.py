# Given two binary strings a and b, return their sum as a binary string.
# Approach two: Count instances of "1" and allow carry to equal on. Append all "1"s to a list. 
# and count instances (list length). 

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
          currentSum = []
          if a != "":
            if a[-1] == "1":
              currentSum += ["1"]
            a = a[:-1]
          if b != "":
            if b[-1] == "1":
              currentSum += ["1"]
            b = b[:-1]

          if carry == True:
            currentSum += ["1"]

          currentSumLen = len(currentSum)

          if currentSumLen == 3:
            result += "1"
            carry = True
          elif currentSumLen == 2:
            result += "0"
            carry = True
          elif currentSumLen == 1:
            result += "1"
            carry = False
          elif currentSumLen == 0:
            result += "0"
            carry = False
        if carry == True:
          result += "1"
        return result[::-1]

a = "1011"
b = "1010"
s = Solution()
print(s.addBinary(a, b))