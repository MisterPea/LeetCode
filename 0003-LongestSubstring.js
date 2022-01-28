/**
 * @param {string} s
 * @return {number}
 */
function lengthOfLongestSubstring(s) {
  const alphaObject = {}
  let maxLength = 0;
  i = 0;
  for(let j = 0; j < s.length; j += 1) {
    if(alphaObject[s[j]] !== undefined) {
      i = Math.max(alphaObject[s[j]], i)
    }
    maxLength = Math.max(maxLength, j - i + 1)
    alphaObject[s[j]] = j + 1
  }
  return maxLength
};
console.log(lengthOfLongestSubstring('aab'))