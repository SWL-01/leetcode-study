class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for first_elemnet in range(0, len(nums) - 1):
            for second_element in range(first_elemnet + 1, len(nums)):
                if nums[first_elemnet] + nums[second_element] == target:
                    result.append(first_elemnet)
                    result.append(second_element)
                    return result
