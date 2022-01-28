/* 
 * Explanation (Kadane's Algorithm): We loop through the array by first setting the max and localSubarray to the
 * first array element.
 * For the localSubarray we set it to the max between the current element
 * or the localSubarray plus the current element.
 * For the maxSubarray, we find the max between the current max and the updated localSubarray.
 * 
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
function maxSubArray(nums) {
  let maxSubarray = nums[0];
  let localSubarray = nums[0];
  for(let j = 1; j < nums.length; j += 1) {
    localSubarray = Math.max(nums[j], localSubarray + nums[j])
    maxSubarray = Math.max(localSubarray, maxSubarray)
  }
  return maxSubarray
};

console.log(maxSubArray([-2]))