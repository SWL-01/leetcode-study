# top to bottom dynamic programming
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        dp0 = cost[0]
        dp1 = cost[1]

        # third step
        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cur

        return min(dp0, dp1)
