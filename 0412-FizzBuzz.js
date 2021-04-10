/**
 * Given an integer n, return a string array answer (1-indexed) where:
 * answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
 * answer[i] == "Fizz" if i is divisible by 3.
 * answer[i] == "Buzz" if i is divisible by 5.
 * answer[i] == i if non of the above conditions are true.
 * 1 <= n <= 10**4
 * @param {number} n
 * @return {string[]}
 */
 const fizzBuzz = (n) => {
    const output = [];
    const three = (i) => {
        return i % 3 === 0;
    }
    const five = (i) => {
        return i % 5 === 0;
    }
    for (i = 1; i <= n; i++) {
        let localString = ''
        if (three(i)) {
            localString += 'Fizz'
        }
        if (five(i)) {
            localString += 'Buzz'
        }
        if (!three(i) && !five(i)) {
            localString = i.toString()
        }
        output[i - 1] = localString
    }
    return output
};

fizzBuzz(24);