/**
 * Given an integer array `nums` sorted in non-decreasing order,
 * return an array of the squares of each number sorted in non-decreasing order.
 * i.e. [-4, -1, 0, 3, 10] --> [0, 1, 9, 16, 100]
 * @param {number[]} nums Input array sorted in increasing order
 * @return {number[]}
 */
var sortedSquares = (nums) => {
    let p1 = 0;
    let p2 = nums.length-1;
    var newArray = [];
    const recursiveSortSquare = (p1, p2) => {
        if (p1 <= p2) {
            var tempP1 = Math.abs(nums[p1]);
            var tempP2 = Math.abs(nums[p2]);
            if (tempP1 < tempP2) {
                newArray.push(tempP2 ** 2)
                p2--
            } else if (tempP1 > tempP2) {
                newArray.push(tempP1 ** 2)
                p1++
            } else {
                if (p1 !== p2) {
                    newArray.push(tempP1 ** 2, tempP2 ** 2)
                    p1++
                    p2--
                } else {
                    newArray.push(tempP1 ** 2)
                    p1++
                }
            }
            return recursiveSortSquare(p1,p2)
        } else {
            return newArray.reverse()
        }
    }
    return recursiveSortSquare(p1,p2)
}

