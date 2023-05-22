# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        ways = 0
        n1 = 1
        n2 = 2

        # A loop that iterates n-2 times
        for i in range(3, n + 1):
            ways = n1 + n2
            n1 = n2
            n2 = ways

        return ways
