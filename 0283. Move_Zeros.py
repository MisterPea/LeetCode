# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array
# e.g. [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        i = nums_length - 1
        while i >= 0:
            if nums[i] == 0:
                nums += [0]
                del nums[i]
            i -= 1
        return nums
