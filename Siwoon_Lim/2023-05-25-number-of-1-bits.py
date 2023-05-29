# Time complexity: O(log n) -> depending on the number of bits 'n'.
# Space complexity: O(1).

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += (n & 1)
            n = n >> 1
        return count
