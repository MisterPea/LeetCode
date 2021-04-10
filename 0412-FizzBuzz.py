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
        fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}
        output = []
        for i in range(1, n + 1):
            localString = ''
            for key in fizz_buzz_dict.keys():
                if i % key == 0:
                    localString += fizz_buzz_dict[key]
            if localString == '':
                localString = str(i)
            output += [localString]
        return output
