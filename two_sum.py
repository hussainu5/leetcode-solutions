class Solution(object):
    def twoSum(self, nums, target):


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i in range(len(nums)):
            num = nums[i]
            checker = target - num
            if checker in lookup:
                return [lookup[checker], i]
            lookup[num] = i