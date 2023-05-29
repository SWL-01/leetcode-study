from bisect import insort_left


# Time complexity: O(n log n)
# Space complexity: O(n)

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort(reverse=False)
        while stones:
            s1 = stones.pop()
            # If x == y, both stones are destroyed
            if not stones:
                return s1
            s2 = stones.pop()
            # If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x
            if s1 > s2:
                # insert the element s1 - s2 value
                insort_left(stones, s1 - s2)
        return 0
