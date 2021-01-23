# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(nums)):
            inverse = target - nums[i]
            if inverse in nums and nums.index(inverse) != i:
                return [i, nums.index(inverse)]


nums = [3, 2, 4]
target = 6
s = Solution().twoSum(nums, target)
