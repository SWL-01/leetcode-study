class Solution(object):
    # if there is a duplicate element then set function
    # will give a list which has length less than the actual list

    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums)) or False
