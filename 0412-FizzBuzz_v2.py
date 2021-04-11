'''
 * Given an integer n, return a string array answer (1-indexed) where:
 * answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
 * answer[i] == "Fizz" if i is divisible by 3.
 * answer[i] == "Buzz" if i is divisible by 5.
 * answer[i] == i if non of the above conditions are true.
 * 1 <= n <= 10**4
'''
class Solution(object):
    def fizzBuzz(self, n):
        output = []
        for i in range(1, n + 1):
            def recursiveFizzBuzz():
                if i % 3 == 0 and i % 5 == 0:
                    return 'FizzBuzz'
                if i % 3 == 0:
                    return 'Fizz'
                if i % 5 == 0:
                    return 'Buzz'
                return str(i)
            output += [recursiveFizzBuzz()]
        return output
           
Solution().fizzBuzz(20)