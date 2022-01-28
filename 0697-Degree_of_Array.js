/* 
 * Given a non-empty array of non-negative integers nums, the degree of this array is defined
 * as the maximum frequency of any one of its elements.
 * Your task is to find the smallest possible length of a (contiguous)
 * subarray of nums, that has the same degree as nums.
 * e.g. [1, 2, 2, 3, 1, 4, 2] returns 6, because of three 2 and their breadth is 6
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
function findShortestSubArray(nums) {
  const seenObj = {}
  for (let i = 0; i < nums.length; i += 1) {
    if (seenObj[nums[i]] !== undefined) {
      seenObj[nums[i]].push(i)
    } else {
      seenObj[nums[i]] = [i]
    }
  }

  let currentMaxMin = { length: undefined, breadth: undefined }

  const deg = Object.values(seenObj)

  for (let k = 0; k < deg.length; k += 1) {
    let currentLength = deg[k].length
    let currentBreadth = (deg[k][currentLength - 1] - deg[k][0]) + 1
    if (currentMaxMin.length === currentLength) {
      currentMaxMin.breadth = Math.min(currentBreadth, currentMaxMin.breadth)
    } else if (currentLength >= currentMaxMin.length || currentMaxMin.length === undefined) {
      currentMaxMin.breadth = currentBreadth
      currentMaxMin.length = currentLength
    }
  }
  return currentMaxMin.breadth
};
